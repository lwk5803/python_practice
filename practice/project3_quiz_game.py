import random
import json

questions = [
    {
        "question": "파이썬에서 출력 함수는?",
        "options" : ["print", "show", "display", "output"],
        "answer"  : 1 # 1번이 정답
    },
    {
        "question": "파이썬에서 정수로 변환하는 함수는?",
        "options" : ["str", "float", "int", "object"],
        "answer"  : 3
    },
    {
        "question": "파이썬에서 반복문을 만들기 위해 사용하는 키워드는?",
        "options" : ["if", "else", "def", "for"],
        "answer"  : 4
    },
    {
        "question": "파이썬에서 잘못된 데이터를 입력할 때 나타나는 에러를 잡기 위한 키워드는?",
        "options" : ["class", "try", "Error", "remove"],
        "answer"  : 2
    },
    {
        "question": "파이썬에서 리스트에 들어있는 특정 값을 삭제하는 함수는??",
        "options" : ["remove", "delete", "pop", "cut"],
        "answer"  : 1
    }
    ]
random.shuffle(questions)
score = 0

for idx1, question in enumerate(questions, 1):
    print(f"\n{idx1}번 문제) {question['question']}")
    for idx2, option in enumerate(question['options'], 1):
        print(f"  {idx2}. {option}")
    answer = input("정답 입력")

    try:
        answer = int(answer)
        if answer == question['answer']:
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 {question['answer']}번 입니다.")
    
    except ValueError:
        print("숫자를 입력하세요!")

print(f"최종 점수 : {score}점")

try:
    with open("best_score.json", "r") as f:
        best_score = json.load(f)
except FileNotFoundError:
    best_score = 0 # 파일 없으면 최고기록 0으로 시작

if score > best_score:
    print(f"최고 기록 갱신! {best_score}점 -> {score}")
    with open('best_score.json', 'w') as f:
        json.dump(score, f)
else:
    print(f"최고 기록은 {best_score}점입니다.")