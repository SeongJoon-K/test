# numbers = []

# numbers.append(5)
# print(numbers)


# numbers.append(8)
# print(numbers)


# numbers.append(10)
# print(numbers)

# numbers.insert(0,0)
# print(numbers)

# 원소 빼기

numbers = [1,2,3,4,5,6,7,8]

del numbers[3]
print(numbers)

# 인덱스 4부터 마지막 값까지 삭제

del numbers[4:]
print(numbers)

# sorted 함수

number = [412,463,4,6,7,3,2,3456,1,60]
number = sorted(number)

print(number)

# 알파벳 연결

alphabet1 = ["a","b","c"]
alphabet2 = ["d","e","f"]
alphabet = alphabet1 + alphabet2

print(alphabet)