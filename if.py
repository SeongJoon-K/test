temp = -1

if temp <= 5:
    print("내복, 긴팔 입러")
elif temp <= 10:
    print("긴팔, 자켓 입어")
elif temp <= 15 :
    print("긴팔만")
else :
    print("반팔입어라")

grade = int(input())

if grade >= 90 :
    print("You get an A.")
elif grade >= 80 :
    print("You get an B.")
elif grade >= 70 :
    print("You get an C.")
elif grade >= 60 :
    print("You get an D.")
else :
    print("You get an F.")

i = 8
while i <= 100 :
    if i % 8 == 0 :
        if i % 12 == 0 :
            i += 8
        else :
            print(i)
            i += 8
    

# 1000보다 작은 2,3 배수의 총합 구하기

sum = 0
i = 1
while i < 1000 :
    if i % 2 == 0 :
        sum += i
        i += 1
    elif i % 3 == 0 :
        sum += i
        i += 1
    else :
        i += 1
print(sum)

#if while 연습 120의 약수 구하기
# 정수 120의 약수

i = 1

while i <= 120 :
    if 120 % i == 0:
        print(i)
        i += 1
    else :
        i += 1

print("120의 약수는 총 16개입니다.")

# codeit 은마아파트와 이자

before_year = 0
rate_plusmoney = 50000000
wongm = 0

while before_year < 28:
    rate_plusmoney += rate_plusmoney * 0.12
    before_year += 1

print(rate_plusmoney)
