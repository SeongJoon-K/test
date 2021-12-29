from random import randint

num_try = 5
answer = randint(1,20)
#print("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요 : {}".format(num_try,x))
i = 1

while i <= 5 :
    x = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요 :" %(num_try-i)))
    if answer == x :
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." %i)
        break
    else :
        if answer <= x :
            print("Down")
            i += 1
        else :
            print("Up")
            i += 1
        
