#a =1
#b =2

def calc():
    #global a, b
    a =3
    b =5
    def mul_add(x):
        return a *x +b
    return mul_add

# a =5
#print(a)
c =calc() # 여기는 calc()가 실행되고
#print(a)
#a =1
print(c(1), c(2), c(3), c(4), c(5)) # 여기는 calc안 mul_add만 실행된다.
#print(a)
