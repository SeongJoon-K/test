from random import randint

number = []
i = 0

while i < 3 :
    new_number = randint(0,9)
    print(new_number)
    number.append(new_number)
    i += 1

print(number)

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("세 수를 하나씩 차례대로 입력하세요.")


# i = 1
# pick = []
# while i <= 3 :
#     num = int(input("%d번째 수를 입력하세요: " %i))
#     pick.append(num)