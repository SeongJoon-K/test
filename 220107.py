# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환
i = 0
while i <= 5 :
    sample_temperature_list[i] = fahrenheit_to_celsius(sample_temperature_list[i])
    i += 1
# 코드를 입력하세요.


# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(sample_temperature_list))



# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    return won / 1000

# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):
    return dollars * 125

# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))
 
# amounts를 원(￦)에서 달러($)로 바꿔주기
i = 0
while i < len(amounts) :
    amounts[i] = krw_to_usd(amounts[i])
    i += 1

print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔(￥)으로 바꿔주기

k = 0
while k < len(amounts):
    amounts[k] = usd_to_jpy(amounts[k])
    k += 1

# 엔(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))



# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
i = 1
while True :
    numbers.append(i)
    i += 1
    if i == 11 :
        break
print(numbers)
    
# # numbers에서 홀수 제거
k = 0
while k <= 9 :
    numbers.remove(1+k)
    k += 2
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0,20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)