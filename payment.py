def calculate_change(payment, cost):
    x = (payment - cost) // 50000
    y = (payment - cost-x*50000) // 10000
    z = (payment - cost-x*50000-y*10000) // 5000
    h = (payment - cost-x*50000-y*10000-z*5000) // 1000
    
    print("50000원 지폐 : {}장".format(x))
    print("10000원 지폐 : {}장".format(y))
    print("5000원 지폐 : {}장".format(z))
    print("1000원 지폐 : {}장".format(h))
    
calculate_change(100000,32000)

