import turtle as t
import random
import math


def _dstnc(x) :#거리
   return (40000-x**2)**(1/2)

def _twinkle(x) :#반짝반짝
    for i in range(0,10):
        deg = random.randint(0,359)
        dst = random.randint(0,7)
        x.right(deg)
        x.fd(dst)



_col = ['red','orange','yellow','green','blue','purple']

for i in range(0,5):
    try :
        n = int(input("정수 1 이상 입력 : "))
    except :
        print("제대로 입력하시오.")
        continue;
    break;
else : exit(0)

t.Screen().bgcolor('grey')

_tur = [];
for i in range(0,2*n):              #2n개 생성
    _tur.append(t.Turtle())
    _tur[i].color(_col[random.randint(0,5)])
    _tur[i].speed(0)
    #if(i%2==0) : print(i//2)
    

for j in range(0,n):
    i = 2*j
    deg = random.randint(0,359)     #
    _tur[i].right(deg)              #
    _tur[i].fd(random.randint(0,5)) #
    _tur[i].left(deg)               #두점사이거리 조금벌리기   
    
    deg = random.randint(0,359)     #방향랜덤 조정
    _tur[i].right(deg)
    _tur[i+1].right(deg)

    R = random.randint(0,200)       #함수에 따른 랜덤거리이동
    dst = _dstnc(R)
    print(dst)
    _tur[i].fd(dst)
    _tur[i+1].fd(dst)
    #_twinkle(_tur[i])
    #_twinkle(_tur[i+1])
    
    

print("정상종료")
    
