def myself(name, age, nationality = "한국"):
    print("이름 %s" %name)
    print("나이 %d" %age)
    print("국적 %s" %nationality)


# myself("코드잇", 1)
# myself("코드잇", 1, "미국")

# x = x + 1
# x += 1

# x = x + 2 
# x += 2

# x = x*2
# x *= 2

ll=[]
for i in range(10):
    ll.append(i*i)

sq_list = [i*i for i in range(10)]

print(f'기존 코드로 만든 리스트 : {ll}')
print(f'list comprehension : {sq_list}')

def my_function():
    x=3
    print(x)