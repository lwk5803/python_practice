import pandas as pd

# # # 딕셔너리로 DataFrame 만들기

# # data = {
# #     "이름": ["철수", "영희", "민수", "지영"],
# #     "나이": [65, 72, 58, 80],
# #     "등급": ["A", "B", "A", "C"],
# #     "출석횟수": [20, 15, 22, 8]
# # }

# # df = pd.DataFrame(data)
# # print(df)

# # #* 특정 열 전체 가져오기
# # print(df['이름']) # 이름 열 전체
# # print(df['출석횟수'])

# # #* 여러 열 가져오기
# # print(df[['이름', '출석횟수']])

# # #* 특정행 가져오기
# # print(df.iloc[0]) # 첫 번째 행
# # print(df.iloc[-1]) # 마지막 행

# # #* 조건으로 필터링 (엑셀 필터 기능과 같음)
# # print(df[df['나이'] >= 70]) # 70세 이상만
# # print(df[df['등급'] == "A"]) # 등급이 A인 사람만

# # #* 기본통계
# # print(df['출석횟수'].sum()) # 합계
# # print(df['출석횟수'].mean()) # 평균
# # print(df['출석횟수'].max()) # 최댓값
# # print(df["출석횟수"].min()) # 최솟값
# # print(df['나이'].count()) # 개수
# # print(df.describe()) # 전체 통계 요약 한번에

# #! 연습문제 16

# data = {
#     "이름": ["김복순", "이정호", "박영자", "최민철", "정순희", "강동원"],
#     "나이": [72, 65, 80, 58, 75, 68],
#     "프로그램": ["요가", "컴퓨터", "요가", "원예", "컴퓨터", "원예"],
#     "출석횟수": [18, 12, 5, 20, 8, 15],
#     "전체횟수": [20, 20, 20, 20, 20, 20]
# }

# df = pd.DataFrame(data)

# print(df['이름'].count()) # 6명
# print(df['출석횟수'].mean()) # 13회
# print(df[df['출석횟수'] < 10]) # 2명

# df['참여율'] = round(df['출석횟수'] / df['전체횟수'] * 100, 1)
# print(df)

# df['관리필요'] = df['참여율'].apply(lambda x: "요관리" if x < 60 else "정상")
# print(df)

# # df.to_excel('이용자현황.xlsx', index=False)

# # #* 프로그램별 평균 출석 횟수
# # print(df.groupby("프로그램")["출석횟수"].mean())

# # #* 프로그램별 인원수
# # print(df.groupby("프로그램")["이름"].count())

# # #* 프로그램별 여러 통계 한번에
# # print(df.groupby("프로그램")['출석횟수'].agg(["mean", "sum", "count"]))

# #! 연습문제 17
# print(df.groupby("프로그램")["참여율"].mean())

# fail_list = df[df['관리필요'] == '요관리']

# print(fail_list.groupby("프로그램")['이름'].count())

# df.groupby("프로그램")['출석횟수'].agg(["mean", "sum", "count"]).to_excel('프로그램별통계.xlsx', index=False)


#! 연습문제 18

# 보고서에 들어가야 할 내용:
# 1. 전체 이용자 현황 (이름, 나이, 프로그램, 참여율, 관리필요 여부)
# 2. 프로그램별 통계 (평균 참여율, 인원수)
# 3. 요관리 대상자 명단

# 여러 시트에 저장하는 방법

data = {
    "이름": ["김복순", "이정호", "박영자", "최민철", "정순희", "강동원", "윤미래", "한지수"],
    "나이": [72, 65, 80, 58, 75, 68, 70, 63],
    "프로그램": ["요가", "컴퓨터", "요가", "원예", "컴퓨터", "원예", "요가", "컴퓨터"],
    "출석횟수": [18, 12, 5, 20, 8, 15, 16, 19],
    "전체횟수": [20, 20, 20, 20, 20, 20, 20, 20]
}

df = pd.DataFrame(data)

# 참여율 열 추가(소숫점 첫째 자리)

df['참여율'] = round(df['출석횟수'] / df['전체횟수'] *100, 1)

# 관리필요 열 추가(참여율 60% 미만"요관리", 이상"정상")
df['관리필요'] = df['참여율'].apply(lambda x : "요관리" if x < 60 else "정상")

# 3개의 시트를 저장
with pd.ExcelWriter('월간출석현황.xlsx') as writer:
    df.to_excel(writer, sheet_name='전체현황', index=False)
    
    # 프로그램별 통계
    stats = df.groupby("프로그램")['참여율'].agg(["mean", "count"])
    stats.to_excel(writer, sheet_name='프로그램별통계')
    
    # 요관리 대상자
    fail_df = df[df['관리필요'] == '요관리']
    fail_df.to_excel(writer, sheet_name='요관리대상자', index=False)