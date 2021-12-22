name = "James"
age = 32


# print("이름 {} 나이 {}".format(name, age))

# 새로운 f-string 방식
print(f"제 이름은 {name}이고 {age}살입니다.")


# 문자열 포맷팅 실습과제

wage = 5
korean_wage = 5710.8
exchange_rate = korean_wage/wage

print(f"{1}시간에 {wage}달러 벌었습니다.")
print(f"{5}시간에 {wage*5}달러 벌었습니다.")
print(f"{1}시간에 {korean_wage}달러 벌었습니다.")
print(f"{5}시간에 {korean_wage*5}달러 벌었습니다.")

# 명제 == 참 거짓이 확실한 것


## 불린 연산 boolean
print(True) # 이면 불린연산이고 
print("True") # 이면 문자열이다
print(not True) # True를 False로 만듬
print(not False) # False를 True로 만듬

print(type(3)) # int형 취급 
print(type(3.0)) #float 형 취급

print(type("True"))
print(type(True))


# 함수의 실행순서

def square(x):
    return x * x

print("함수 호출전")
print(square(3)+square(4))
print("함수 호출 후")


# return 문의 역할을 무엇인가
# 1. 값을 돌려주는 것
# 2. 함수를 즉시 종료시키는 것 

# print, return의 차이

def print_square(x):
    print(x*x)

def get_square(x):
    return x * x

get_square(3)