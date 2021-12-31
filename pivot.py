# first = 1
# second = 1
# third = first + second

# sum = 0
# sum_b = 0
# sum_bb = 1
# i = 1
# while i <= 20 :
#     if i <= 1 :
#         print(first)
#         i += 1
#     elif i <=2 :
#         print(second)
#         i += 1
#     elif i == 3:
#         sum_b = first + second
# #         i += 1
# #     else :
# #         sum = sum_b + sum
# #         print(sum)
# #         i += 1


# i = 1 ## 첫 번쨰항
# k = 1 # 두 번쨰 항
# sum = 0 # 총 합
# sum_b = 0 # 이전 항

# # 세 번째 항 부터 

# while i <= 21 :
#     if i == 1 :
#         print(1)
#         i += 1
#     elif i == 2 :
#         print(i+i)
#         sum_b = i
#         i += 1
#     elif i >= 3 :
#         sum_b = sum
#         sum = sum + sum_b
#         print(sum)
#         i += 1



# # 첫번쨰항은 1 두번째항도 1
# 세번째항 = 첫번째 + 두번째
# 네번째항 = 세번째항 + 두번째항
# 다섯항 = 네번쨰 + 세번째

# i = 1 
# a = 1 # 첫 번째 항
# b = 1 # 두 번째 항
# sum = 1
# sum_b = 1

# while i <= 20 :
#     if i == 1 :
#         print(a)
#         i += 1
        
       
#     elif i == 2 :
#         print(b) 
#         i += 1
        
#     else :
#         for i in range (1, 20):
#             sum, sum_b = sum_b, sum+sum_b
            
#             i += 1
#             print(sum)


#상수 
count = 20
#변수
current = 1
previous = 0
i = 0

while i < count :
    print(current)
    
    temp = previous
    previous = current
    current = current + temp

    i += 1
n=int(input())
for _ in range(n):
    a,b=input().strip().split()
    print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))

