# 화씨에서 섭씨로 바꿔주는 함수
i = 0
sum_list = []
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
        

# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

# 화씨에서 섭씨로 변환
i = 0
while i <= 5 :
    sample_temperature_list[i] = fahrenheit_to_celsius(sample_temperature_list[i])
    i += 1

print("섭씨 온도 리스트: " + str(sample_temperature_list))

