# temp = -1

# if temp <= 5:
#     print("내복, 긴팔 입러")
# elif temp <= 10:
#     print("긴팔, 자켓 입어")
# elif temp <= 15 :
#     print("긴팔만")
# else :
#     print("반팔입어라")

# grade = int(input())

# if grade >= 90 :
#     print("You get an A.")
# elif grade >= 80 :
#     print("You get an B.")
# elif grade >= 70 :
#     print("You get an C.")
# elif grade >= 60 :
#     print("You get an D.")
# else :
#     print("You get an F.")

i = 8
while i <= 100 :
    if i % 8 == 0 :
        if i % 12 == 0 :
            i += 8
        else :
            print(i)
            i += 8
    