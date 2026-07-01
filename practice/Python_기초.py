# 1단계 : 변수와 출력
name = "철수"
age = 20
height = 175.5

print(name)
print("나이", age)

# 문자열(str) : "안녕" 처럼 따옴표로 감싼것
# 정수(int) : 10, -5
# 실수(float) : 3.14
# 불리언(bool) : True, False

# 변수 타입이 헷갈리면 type()으로 확인할 수 있습니다.
print(type(age)) # <class 'int'>

# 연습문제 1
# 1. city라는 변수에 본인이 살고 싶은 도시 이름을 문자열로 저장하세요.
city = "서울"

# 2. temperature라는 변수에 그 도시의 기온(숫자)을 저장하세요.
temperature = 32

# 3. print()를 이용해서 "city는 temperature도입니다" 형태의 문장을 출력하세요.

print(f"{city}는 {temperature}도입니다.")

name = input("이름을 입력하세요: ")  # input으로 받은 값은 항상 **문자열**
print(f"안녕하세요, {name}님!")

age = input("나이를 입력하세요: ") # 문자열로 들어옴
age = int(age) # 정수로 변환

# 연습문제 2
# input()으로 사용자에게 좋아하는 숫자를 입력받아 num이라는 변수에 저장하세요
num = input("좋아하는 숫자: ")
# num을 정수형으로 변환하세요. 
num = int(num)
# 그 숫자에 10을 더한 결과를 출력하세요.
print(num + 10)

age = 20
if age >= 20:
    print("성인입니다")
elif age>= 13:
    print("청소년입니다")
else:
    print("어린이입니다")

score = 85
if score >= 90 and score <= 100:
    print("A등급")

score = input("시험 점수를 입력하세요: ")
score = int(score)

if score >= 90:
    print("A등급")
elif score >= 70 and score < 90:
    print("B등급")
else:
    print("C등급")

for i in range(5):
    print(i) # 0, 1, 2, 3, 4 출력
 
for i in range(1, 10, 2): #range(start, stop, step) 형태
    print(i) #1, 3, 5, 7, 9 출력

count = 0
while count < 5:
    print(count)
    count += 1 # count = count + 1과 같음
total = 0
for i in range(1, 11):
    total += i
    print(total)

total = 0
count = 1
while count <= 10:
    total += count
    count += 1
    print(total)

fruits = ["사과", "바나나", "딸기"]
print(fruits[0]) # 사과(인덱스는 0부터 시작)
print(fruits[-1]) # 딸기(마지막 요소)

fruits.append("포도") # 리스트 끝에 추가
print(fruits)

print(len(fruits)) # 리스트 길이 : 4

for fruit in fruits:
    print(fruit)

fruits[0] = "오렌지" # 첫번째 요소 변경
fruits.remove("바나나") # 특정 값 삭제

movies = ['A', 'B', 'C']

for movie in movies:
    print(movie)

movies.append('D')
print(len(movies))

person = {
    "name": "철수",
    "age": 20,
    "city": "서울"
}

print(person['name'])
print(person['age'])

person['job'] = '학생' # 새 키 추가
person['age'] = 21 # 기존 값 수정

for key, value in person.items(): # 딕셔너리 전체 반복 .items()
    print(key, ":", value)

print(person.get('phone')) # 없으면 None 반환(에러 안남)

me = {
    "name" : "이원경",
    "age" : 33,
    "hobby" : "Game"
}

for key, value in me.items():
    print(key, ":", value)

me['hobby'] = 'Music'

print(me["hobby"])

def great(name):
    print(f"안녕하세요, {name}님!")

great("철수") # 함수 호출

def add(a, b):
    return a + b # 출력값을 함수 밖으로 보내줌

result = add(3, 5)
print(result)

def greet(name="익명"): # 파라미터 기본값 설정
    print(f"안녕하세요, {name}님!")

greet()
greet("영희")

def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
    
for num in range(1, 11):
    if is_even(num) == True:
        print(num)


result = []
for num in range(1, 11):
    if is_even(num):
        result.append(num)

result = [num for num in range(1, 11) if is_even(num)]
print(result)

students = [
    {"name": "철수", "score":80},
    {"name": "영희", "score":92},
    {"name": "민수", "score":60}
]
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return 'B'
    else:
        return 'C'

for student in students:
    name = student['name']
    score = student['score']
    grade = get_grade(score)
    print(f"{name}: {grade}")

students = [
    {"name": "철수", "score": 80},
    {"name": "영희", "score": 92},
    {"name": "민수", "score": 60},
    {"name": "지영", "score": 75},
    {"name": "수민", "score": 45}
]


total = 0
for student in students:
    total += student['score']
    avg = total / len(students)
    avg = round(avg, 2)
print(f"평균 : {avg}") 

above_avg = []
for student in students:
    if student['score'] > avg:
        above_avg.append(student['name'])
print(above_avg)

falied = False
for student in students:
    if student['score'] < 60:
        falied = True

if falied:
    print("낙제생이 있습니다.")
else:
    print("낙제생이 없습니다.")

top = 0
top_name = ""
for student in students:
    name = student['name']
    score = student['score']
    if score > top:
        top = score
        top_name = name

print(f"최고 점수: {top_name}({top}점)")

employees = [
    {"name": "김대표", "salary": 5000},
    {"name": "이부장", "salary": 4200},
    {"name": "박과장", "salary": 3500},
    {"name": "최사원", "salary": 2800},
    {"name": "정인턴", "salary": 2000}
]

total = 0
for employee in employees:
    total += employee['salary']
    avg = total / len(employees)
    avg = round(avg, 2)
print(avg)

employee_list = []
for employee in employees:
    name = employee['name']
    salary = employee['salary']
    if salary < avg:
        employee_list.append(name)
print(employee_list)

law_employee = False
for employee in employees:
    name = employee['name']
    salary = employee['salary']
    if salary < 3000:
        law_employee = True

if law_employee:
    print("저연봉자가 있습니다")
else:
    print("저연봉자가 없습니다.")

bottom_salary = 10000
bottom_name = ""

for employee in employees:
    name = employee["name"]
    salary = employee['salary']
    if salary < bottom_salary:
        bottom_salary = salary
        bottom_name = name

print(f"최저연봉 : {bottom_name}({bottom_salary})")

num = int(input("숫자를 입력하세요: "))
print(10/num)

try:
    unm = int(input("숫자를 입력하세요: "))
    result = 10 / num
    print(result)
except ValueError:
    print("숫자가 아닌 값을 입력하였습니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

try:
    num = int(input("숫자: "))
except ValueError:
    print("숫자가 아닙니다.")
else:
    print("입력 성공")
finally:
    print("프로그램을 종료합니다.")

try:
    num1 = int(input("첫 번재 숫자를 입력하세요: "))
    num2 = int(input("두 번재 숫자를 입력하세요: "))
    print(num1 / num2)
except ValueError:
    print("숫자만 입력해주세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

inventory = {
    "사과": 10,
    "바나나": 5,
    "딸기": 0
}
try:
    fruit = input("과일 이름을 입력하세요")
    print(f"{fruit} 재고 : {inventory[fruit]}개")
except KeyError:
    print("재고 목록에 없는 과일입니다.")

class Student:                                  # 새로운 틀 정의
    def __init__(self, name, score):            # 생성자 / 자동으로 실행, 초기설정
        self.name = name                        # 'self' 객체 자신 ==> 클래스 안의 모든 함수(메서드)는 자기 자진을 받아야함
        self.score = score                      # self.name -> 객체 자신의 속성(name)에 값을 저장

    def show(self):
        print(f"{self.name}: {self.score}점")

s1 = Student("철수", 90)
s2 = Student("영희", 92)

print(s1.name)
print(s2.score)

class car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = 0
    
    def accelerate(self, amount):
        self.speed += amount # self.speed로 접근

    def show_speed(self):
        print(f"현재 속도: {self.speed}km/h")

my_car = car("BMW")
my_car.accelerate(30)
my_car.show_speed()

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount            

    
    def show_balance(self):
        print(f"예금주 : {self.owner}, 잔액:{self.balance}원")

My_Account = BankAccount("Won")
My_Account.deposit(50000)
My_Account.withdraw(80000)
My_Account.withdraw(20000)
My_Account.show_balance()