def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
 
c = calc() # calc함수가 계속 살아 있는듯
c(1)
c(2)
c(3)
