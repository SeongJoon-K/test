# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)


# sort method 
numbers = [5,3,7,1]
# numbers.sort()
# print(numbers)

# reverse method

numbers.reverse()
print(numbers)

members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

fruit = ["딸기", "당근", "파인애플", "수박", "참외","메론"]
fruit.remove("파인애플")
print(fruit)