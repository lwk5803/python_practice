# === 학생 성적 관리 시스템 ===
# 1. 학생 추가, 2. 전체 학생 조회, 3. 평균 점수 및 등급 조회, 4. 종료

import json

try:
    with open("students.json", "r") as f:
        students = json.load(f)
except FileNotFoundError:
    students = [] # 파일 없으면 빈 리스트로 시작

def get_grade(score):
    if score >= 90:
        return("A")
    elif score >= 70:
        return("B")
    else:
        return("C")

while True:
    print("=== 학생 성적 관리 시스템 ===")
    print('1. 학생 추가')
    print('2. 전체 학생 조회')
    print('3. 평균 및 등급 조회')
    print('4. 학생 검색')
    print('5. 학생 삭제')
    print('6. 종료')
    
    choice = input("선택: ")

    if choice == "1":
        name = input("이름을 입력하세요: ")

        already_exists = False

        for student in students:
            if student['name'] == name:
                already_exists = True

        if already_exists:
            print("이미 등록된 학생입니다.")

        else:
            try:
                score = int(input("점수를 입력하세요: "))
            except ValueError:
                print("점수는 숫자로 입력해주세요.")

            st_dict = {"name": name, "score": score}
            students.append(st_dict)

            with open("students.json", "w") as f:
                json.dump(students, f)

            print(f"{name} 학생이 추가되었습니다.")

    elif choice == "2":
        if not students:
            print("등록된 학생이 없습니다.")

        else:
            for student in students:
                print(f"이름: {student['name']}, 점수: {student['score']}")
 
    elif choice == "3":
        if not students:
            print("등록된 학생이 없습니다.")

        else:
            total = 0

            for student in students:
                total += student['score']

            avg = total / len(students)
            avg = round(avg, 2)

            print("전체 평균 : ", avg)
        
            for student in students:
                print(f"이름:{student['name']}",
                      f"점수:{student['score']}",
                      f"등급: {get_grade(student['score'])}" )


    elif choice == "4":
        name = input("이름을 입력하세요: ")

        found = None

        for student in students:
            if student['name'] == name:
                found = student # 찾으면 학생 딕셔너리 저장
        
        if found:
            print(f"이름: {found['name']}, 점수: {found['score']}, 등급: {get_grade(found['score'])}")

        else:
            print("등록되지 않은 학생입니다.")
    
    elif choice == "5":
        name = input("이름을 입력하세요. ")

        found = None

        for student in students:
            if student['name'] == name:
                found = student

        if found:
            students.remove(found)
            with open("students.json", "w") as f:
                json.dump(students, f)

            print(f"{name} 학생이 삭제되었습니다.")

        else:
            print("등록되지 않은 학생입니다.")
    
    elif choice == "6":
        print("프로그램을 종료합니다.")
        break