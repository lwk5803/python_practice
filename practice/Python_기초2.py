
# # * 기존방식
# result = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         result.append(i)

# #? 리스트 컴프리헨션
# result = [i for i in range(1, 11) if i % 2 == 0]
# print(result)

# students = [
#     {"name": "철수", "score":80},
#     {"name": "영희", "score":92},
#     {"name": "민수", "score":60}
# ]

# #* 이름만 추출
# names = [s['name'] for s in students]
# print(names) # ['철수', '영희', '민수']

# #* 80점 이상인 학생 이름만 추출
# high_score = [s['name'] for s in students if s['score'] >= 80]
# print(high_score)

# add = lambda a, b: a + b
# print(add(3, 5))

# #* 점수 기준으로 정렬
# sorted_students = sorted(students, key = lambda s: s['score'])
# print(sorted_students)

# #* 내림차순 (높은 점수 먼저)
# sorted_students = sorted(students, key=lambda s: s['score'], reverse=True)
# print(sorted_students)

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, numbers)) #* map() 리스트에 모든 요소에 함수 내용을 적용
# print(squared)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(lambda x: x % 2 == 0, numbers)) #* filter 조건에 맞는 요소만 걸러내기
# print(evens)

#! 연습문제
students = [
    {"name": "철수", "score": 80},
    {"name": "영희", "score": 92},
    {"name": "민수", "score": 60},
    {"name": "지영", "score": 75},
    {"name": "수민", "score": 45}
]

names = [x['name'] for x in students]
print(names)

pass_students = [x['name'] for x in students if x['score'] >= 70]
print(pass_students)

sorted_list = sorted(students, key=lambda x: x['score'], reverse=True)
print(sorted_list)

map_list = list(map(lambda x: x+5, [x['score'] for x in students]))
print(map_list)

filter_list = list(filter(lambda x : x['score'] < 60, students))
print(filter_list)