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
#         i += 1
#     else :
#         sum = sum_b + sum
#         print(sum)
#         i += 1


i = 1
sum = 0
sum_b = 2
while i <= 20 :
    if i == 1 :
        print(1)
        i += 1
    elif i == 2 :
        print(i+i)
        sum_b = i
        i += 1
    elif i >= 3 :
        sum_b = sum
        sum = sum + sum_b
        print(sum)
        i += 1

    