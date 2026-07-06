import numpy as np
import pandas as pd

#* **ndarray**

#파이썬 리스트
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list1 + list2) # 두 리스트의 값이 이어붙어서 출력됨

# numpy 배열
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
print(arr1 + arr2) # 요소별로 덧셈해줌

# 리스트로 배열 만들기
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) # numpy ndarray

# 2차원 배열 (행렬)
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr_2d)
print(arr_2d.shape)  # (3, 3) ==> 3행 3열

# 자주쓰는 배열 생성 방법
print(np.zeros(5))  # [0. 0. 0. 0. 0.] 0으로 채운 배열
print(np.ones(5)) # [1. 1. 1. 1. 1.] 1로 채운 배열
print(np.arange(1, 11)) # [ 1 2 3 4 5 6 7 8 9 10] range와 비슷
print(np.arange(0, 1, 0.2)) # [0. 0.2 0.4 0.6 0.8] # 실수도 가능

arr = np.array([1, 2, 3, 4, 5])

# 배열 전체에 한번에 연산 (파이썬 리스트로는 불가능!)

print(arr + 10) # [11 12 13 14 15]
print(arr * 2) # [2 4 6 8 10]
print(arr ** 2) # [1 4 9 16 25]
print(arr / 2) # [0.5 1. 1.5 2. 2.5]

# 두 배열 간 연산
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)
print(arr1 * arr2) 

# 통계함수
arr = np.array([18, 12, 5, 20, 8, 15, 16, 19])

print(np.sum(arr))    # 합계: 113
print(np.mean(arr))   # 평균: 14.125
print(np.max(arr))    # 최댓값: 20
print(np.min(arr))    # 최솟값: 5
print(np.std(arr))    # 표준편차
print(np.median(arr)) # 중앙값 15.5

# 인덱싱과 슬라이싱
arr = np.array([10, 20, 30, 40, 50])

# 인덱싱(파이썬 리스트와 동일)
print(arr[0]) # 10
print(arr[-1]) # 50

# 슬라이싱
print(arr[1:4]) # [20 30 40]
print(arr[:3])  # [10 20 30]
print(arr[::2]) # [10 30 50] 두 칸씩 건너뛰기

# 2차월 배열 인덱싱
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr_2d[0, 1]) # 2 -> 0행 1열
print(arr_2d[1, :]) # [4 5 6] -> 1행 전체
print(arr_2d[:, 0]) # [1 4 7] -> 0열 전체
print(arr_2d[0:2, 1:]) # [[2 3] [5 6]] -> 0~1행, 1~2열

# 조건 필터링

arr = np.array([18, 12, 5, 20, 8, 15, 16, 19])

# 조건으로 필터링 (pandas의 필터링과 같은 원리!)
print(arr[arr >= 15]) # [18 15 16 19] 15 이상인 값만
print(arr[arr < 10]) # [5 8] 10 미만인 값만

# 조건 확인
print(arr >= 15) # [Ture or False]

#! 연습문제 20

# 8명의 이용자 월간 출석 데이터
attendance = np.array([18, 12, 5, 20, 8, 15, 16, 19])
total = 20 # 전체 수업 횟수

# 전체 출석횟수의 평균 최댓값 최솟값을 출력

print(np.sum(attendance))
print(np.mean(attendance))
print(np.max(attendance))
print(np.min(attendance))

# 참여율 배율을 만들기

att_pct = np.array(attendance / total*100) # attendance가 이미 넘파이 배열이라 굳이 np.array를 안써도 됨
print(att_pct)

# 참여율이 60% 미만인 값만 필터링
print(att_pct[att_pct < 60])

# 참여율이 60% 미만인 이용자가 몇명인지 출력
print(len(att_pct[att_pct < 60]), "명")

# 전체 참여율의 표준편차
print(np.std(att_pct))

# 배열 모양 바꾸기

arr = np.arange(1, 13)
print(arr.shape) # 1차원, 12개

# 3행 4열로 변환
arr_2d = arr.reshape(3, 4)
print(arr_2d)

# -1을 쓰면 자동으로 계산
arr_2d = arr.reshape(3, -1) # 3행, 열은 자동 계산
arr_2d = arr.reshape(-1, 4) # 행은 자동 계산, 4열

# # NumPy 배열 -> pandas DataFrame
attendance = np.array([18, 12, 5, 20, 8, 15, 16, 19])
names= ["김복순", "이정호", "박영자", "최민철", "정순희", "강동원", "윤미래", "한지수"]

df = pd.DataFrame({
    "이름" : names,
    "출석횟수" : attendance,
    "참여율": attendance / 20 * 100
})

# pandas 열 --> NumPy 배열로 변환
arr = df['출석횟수'].to_numpy()
print(type(arr))
print(np.mean(arr))

#! 연습문제 21

names = ["김복순", "이정호", "박영자", "최민철", "정순희", "강동원", "윤미래", "한지수"]
attendance = np.array([18, 12, 5, 20, 8, 15, 16, 19])
total = 20

# attendance를 reshape(2, 4)로 변환해서 출력

print(attendance.reshape(2, 4))

# 참여율 배열 acc_pct를 만드세요.

att_pct = attendance / total * 100

# nmaes, attendance, att_pct를 활용해서 DataFrame을 만드세요

df = pd.DataFrame({
    "이름":names,
    "출석횟수":attendance,
    "참여율":att_pct
})

# df에 관리필요 열을 추가하세요
df['관리필요'] = df['참여율'].apply(lambda x : "요관리" if x < 60 else "정상")

# 평균 참여율 보다 높은 이용자만 필터링해서 출력
print(df[df['참여율'] > np.mean(df['참여율'])])

# 최종현황을 출석환형.xlsx로 저장하세요

df.to_excel('출석현황.xlsx')