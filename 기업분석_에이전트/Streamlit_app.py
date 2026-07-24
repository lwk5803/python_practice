"""
기업분석 LangGraph 에이전트 - Streamlit 웹 UI

기존 CLI 스크립트(기업분석_langgraph_myagent_final_v5_수정중.py)는 건드리지 않고,
딱 2가지만 아주 살짝 손봤습니다.
  1) REPORT_PROMPT / Draft_Report 에 revision_note 연결 (사용자 피드백 실제 반영)
  2) build_graph(checkpointer=None) 처럼 checkpointer를 주입할 수 있게 파라미터 하나 추가

나머지 "웹에서 어떻게 사용자 입력을 받을 것인가"는 전부 이 파일 안에서 처리합니다.
방법은 이렇습니다.

- 기존 코드의 input()이 있던 두 지점(confirm_company_candidate, Review_Draft)을
  "웹 버전" 함수로 새로 만들고, LangGraph의 interrupt()를 사용해 그래프 실행을 멈춥니다.
- 원본 모듈을 import한 뒤, 그 모듈 안의 confirm_company_candidate / Review_Draft
  이름만 몽키패치(런타임 교체)해서 웹 버전으로 바꿔치기합니다.
  -> 원본 파일의 소스코드 자체는 단 한 줄도 안 바꿔도 됩니다.
- MemorySaver 체크포인터로 그래프 상태를 세션(브라우저 탭)별로 저장해두고,
  Streamlit이 매번 스크립트를 처음부터 다시 실행하는 특성에 맞춰
  "멈춘 지점부터 이어서 실행(Command(resume=...))"하는 방식으로 동작합니다.

실행 방법:
    pip install streamlit
    streamlit run streamlit_app.py
"""

import importlib.util
import pathlib
import uuid

import streamlit as st
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command, interrupt

# ------------------------------------------------------------------
# 원본 오케스트레이터 파일 경로
# (같은 폴더에 있다고 가정. 파일명이 다르면 아래 문자열만 바꿔주세요.)
# ------------------------------------------------------------------
AGENT_MODULE_PATH = pathlib.Path(__file__).parent / "기업분석_langgraph_myagent_final_v5_수정중.py"


# ------------------------------------------------------------------
# 웹용 "사용자 확인" 함수들
# 기존 input() 버전과 하는 일은 완전히 동일하지만,
# 콘솔 입력 대신 interrupt()로 그래프를 잠시 멈추고
# Streamlit 화면에서 답을 받아옵니다.
# ------------------------------------------------------------------
def make_web_confirm_company_candidate():
    def web_confirm_company_candidate(candidates_df, query):
        if candidates_df.empty:
            answer = interrupt({"type": "company_not_found", "query": query})
            if answer == "proceed":
                return None
            raise _agentmod.AnalysisAborted(
                f"'{query}' 회사를 찾지 못해 사용자가 분석을 취소했습니다."
            )

        rows = candidates_df.to_dict(orient="records")
        # numpy 타입이 섞여 있으면 화면/직렬화에서 이상하게 나올 수 있어 순수 파이썬 타입으로 정리
        clean_rows = [
            {
                "corp_name": r.get("corp_name"),
                "corp_name_eng": r.get("corp_name_eng"),
                "stock_code": r.get("stock_code"),
                "score": float(r.get("score", 0)),
            }
            for r in rows
        ]

        answer = interrupt(
            {"type": "company_candidates", "query": query, "candidates": clean_rows}
        )
        # answer: 0(없음/힌트만 진행) 또는 1..N(선택한 후보 번호)
        if answer == 0:
            return None
        return rows[int(answer) - 1]

    return web_confirm_company_candidate


def make_web_review_draft():
    def web_Review_Draft(state):
        attempts = state.get("review_attempts") or 0
        draft = state.get("analysis_draft") or ""

        if attempts >= _agentmod.MAX_REVIEW_ATTEMPTS:
            _agentmod.add_note(state, "[Review Draft] 재작성 한도 도달-현재 초안으로 확정")
            state["draft_feedback"] = None
            return state

        answer = interrupt(
            {"type": "draft_review", "draft": draft, "attempts": attempts}
        )
        # answer: {"action": "approve" | "cancel" | "revise", "feedback": "..."}

        if answer.get("action") == "cancel":
            _agentmod.add_note(state, "[Review Draft] 사용자가 초안 검토 단계에서 분석을 취소함")
            raise _agentmod.AnalysisAborted("사용자가 초안 확인 단계에서 분석을 취소했습니다.")

        if answer.get("action") == "approve":
            _agentmod.add_note(state, "[Review Draft] 사용자가 초안을 승인함")
            state["draft_feedback"] = None
            return state

        feedback = (answer.get("feedback") or "").strip()
        state["draft_feedback"] = feedback or "내용을 조금 더 구체적으로 다듬어줘"
        state["review_attempts"] = attempts + 1
        _agentmod.add_note(
            state,
            f"[Review Draft] 사용자 피드백 반영 재작성 요청 ({state['review_attempts']}회차): {state['draft_feedback']}",
        )
        return state

    return web_Review_Draft


# ------------------------------------------------------------------
# 원본 모듈 로드 + 몽키패치 + 그래프 컴파일
# 무거운 리소스(리랭커 모델 로딩 등)가 여기서 한 번만 실행되도록 캐시
# ------------------------------------------------------------------
@st.cache_resource(show_spinner="에이전트를 초기화하는 중입니다 (최초 1회만 시간이 걸립니다)...")
def load_agent():
    spec = importlib.util.spec_from_file_location("agent_core", AGENT_MODULE_PATH)
    agentmod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(agentmod)  # 원본 파일 최상단 코드 실행 (reranker 로딩 등)

    global _agentmod
    _agentmod = agentmod

    # 원본 모듈 안의 두 함수만 웹 버전으로 교체 (원본 파일은 전혀 수정하지 않음)
    agentmod.confirm_company_candidate = make_web_confirm_company_candidate()
    agentmod.Review_Draft = make_web_review_draft()

    checkpointer = MemorySaver()
    graph = agentmod.build_graph(checkpointer=checkpointer)
    return agentmod, graph


_agentmod = None  # load_agent() 실행 후 채워짐 (web_* 함수들이 참조)
agentmod, graph = load_agent()


# ------------------------------------------------------------------
# Streamlit 세션 상태 초기화
# ------------------------------------------------------------------
st.set_page_config(page_title="기업분석 에이전트", layout="centered")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())
if "phase" not in st.session_state:
    st.session_state.phase = "input"  # input -> paused -> done
if "pending_interrupt" not in st.session_state:
    st.session_state.pending_interrupt = None
if "final_report" not in st.session_state:
    st.session_state.final_report = None
if "error" not in st.session_state:
    st.session_state.error = None

config = {"configurable": {"thread_id": st.session_state.thread_id}}


def run_graph(payload):
    """graph.invoke() 실행 후 결과를 세션 상태에 반영.
    interrupt가 걸리면 화면에 물어볼 질문을 저장하고,
    끝까지 실행되면 최종 보고서를 저장한다."""
    try:
        result = graph.invoke(payload, config=config)
    except agentmod.AnalysisAborted as e:
        st.session_state.phase = "done"
        st.session_state.error = str(e)
        return

    if "__interrupt__" in result:
        interrupt_obj = result["__interrupt__"][0]
        st.session_state.pending_interrupt = interrupt_obj.value
        st.session_state.phase = "paused"
    else:
        st.session_state.phase = "done"
        st.session_state.final_report = result.get("final_report")


st.title("📊 LLM 기업분석 에이전트")

# ------------------------------------------------------------------
# 1. 최초 회사명 입력 화면
# ------------------------------------------------------------------
if st.session_state.phase == "input":
    comname = st.text_input("분석할 국내 상장 기업 이름을 입력하세요")
    if st.button("분석 시작", type="primary") and comname:
        state1 = {
            "question": f"{comname} 투자 리스크 분석과 최근 뉴스 3가지만.",
            "company_hint": comname,
            "notes": [],
        }
        with st.spinner("회사 정보를 확인하는 중..."):
            run_graph(state1)
        st.rerun()

# ------------------------------------------------------------------
# 2. 그래프가 interrupt()로 멈춘 경우: 화면에서 답을 받아 이어서 실행
# ------------------------------------------------------------------
elif st.session_state.phase == "paused":
    payload = st.session_state.pending_interrupt

    if payload["type"] == "company_not_found":
        st.warning(f"'{payload['query']}'와 일치하는 상장회사를 DART 목록에서 찾지 못했습니다.")
        col1, col2 = st.columns(2)
        if col1.button("회사명 힌트만으로 계속 진행"):
            with st.spinner("계속 진행 중..."):
                run_graph(Command(resume="proceed"))
            st.rerun()
        if col2.button("분석 취소", type="secondary"):
            with st.spinner("취소 처리 중..."):
                run_graph(Command(resume="abort"))
            st.rerun()

    elif payload["type"] == "company_candidates":
        st.info(f"'{payload['query']}'와 유사한 상장회사 {len(payload['candidates'])}개를 찾았습니다.")
        labels = ["0) 해당 없음 / 회사명 힌트만으로 진행"] + [
            f"{i}) {c['corp_name']} ({c.get('corp_name_eng') or '-'}) · {c['stock_code']} · 유사도 {c['score']:.1f}"
            for i, c in enumerate(payload["candidates"], 1)
        ]
        choice = st.radio("분석할 회사를 선택하세요", labels, index=1 if len(labels) > 1 else 0)
        if st.button("선택 확정", type="primary"):
            idx = labels.index(choice)  # 0 = 힌트만 진행
            with st.spinner("회사 정보를 확인하는 중..."):
                run_graph(Command(resume=idx))
            st.rerun()

    elif payload["type"] == "draft_review":
        st.subheader("초안 미리보기")
        st.markdown(payload["draft"])
        st.caption(f"재작성 시도 {payload['attempts']}회 / 최대 {agentmod.MAX_REVIEW_ATTEMPTS}회")

        action = st.radio(
            "이 초안을 어떻게 할까요?",
            ["확정", "수정 요청", "분석 취소"],
            horizontal=True,
        )
        feedback_text = ""
        if action == "수정 요청":
            feedback_text = st.text_area("수정하고 싶은 내용을 입력하세요")

        if st.button("제출", type="primary"):
            if action == "확정":
                resume_val = {"action": "approve"}
            elif action == "분석 취소":
                resume_val = {"action": "cancel"}
            else:
                resume_val = {"action": "revise", "feedback": feedback_text}
            with st.spinner("반영 중..."):
                run_graph(Command(resume=resume_val))
            st.rerun()

# ------------------------------------------------------------------
# 3. 완료 화면
# ------------------------------------------------------------------
elif st.session_state.phase == "done":
    if st.session_state.error:
        st.error(f"분석이 취소되었습니다: {st.session_state.error}")
    else:
        st.success("분석이 완료되었습니다!")
        st.markdown(st.session_state.final_report)

    if st.button("새로운 회사 분석하기"):
        for k in ["phase", "pending_interrupt", "final_report", "error", "thread_id"]:
            st.session_state.pop(k, None)
        st.rerun()