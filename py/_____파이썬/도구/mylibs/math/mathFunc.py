import random as rd


def genPrime(LEN = 64):
    while 1:
        p = rd.randint(2, 2**LEN-1)
        if not(p & 1):#짝수냐
            continue

        if checkPrime(p):
            break
    return p


def checkPrime(p):
    for i in range(100):
        a = rd.randint(2, p-1)#a < p
        if modpow(a, p-1, p) == 1:
            pass
        else:
            return False
    return True


def modpow(a, b, m):# x = (a^b) % m   #a^b를 a^(100110)식으로 
    if type(a) is not int or \
       type(b) is not int or \
       type(m) is not int:
        return None
    
    res = 1
    while b:
        if b & 1:
            res = (res * a) % m
        b >>= 1
        a = (a**2) % m
    return res

def bin_mod(a, b):#a%b  b가 a길이만큼 늘리고 쉬프트하면서 xor로 최고차항 뺌
    #Rijndael's finite field
    if len(bin(a)) < len(bin(b)):
        return 0, a
    
    gap = len(bin(a)) - len(bin(b))
    pointer = len(bin(a)) - 3
    q = b << gap

    n = 0 # 몫

    a ^= q
    n += 1
    pointer -= 1
    
    for i in range(gap):
        q >>= 1
        n <<= 1
        if a & 1<<pointer:
            a ^= q
            n += 1
        pointer -= 1

    return n, a #몫, 나머지


def bin_mul(q, n, sbox = False):#n을 q의 각항에 분배 #교환법칙되더라
    #q = 1011이라면 q = 1000 ^ 10 ^ 1
    if n > 0xff:
        print('Error in bin_mul ...n')
        return None
    if q > 0xff:
        print('Error in bin_mul ...q')
        return None
    res = 0
    
    while q > 0:
        if q & 1:
            res ^= n
        q >>= 1
        n <<= 1
        if sbox == False and n & 0x100:
            n ^= 0x11b # 100011011 = x^8+x^4+x^3+x+1
    return res


def gcd(x, y):
    if type(x) is not int or \
       type(y) is not int:
        return None
    
    if y == 0:
        return x
    return gcd(y, x%y)


def EEA(a, b):#Extended Euclidean Algorithm
    #r1 == 1일 경우,즉 a,b가 서로소일 경우, s1은 mod b에 대한 a의 역원이 된다.
    if a < b:
        print('a 보다 b가 큼')
        return None, None, None
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        
        r1, r2 = r2, r1 - q*r2
        s1, s2 = s2, s1 - q*s2
        t1, t2 = t2, t1 - q*t2
        
    return s1, t1, r1 #s1은 a의 inverse, t1은 b의 inverse


def EEA2(r1, r2, \
         s1 = 1, s2 = 0, \
         t1 = 0, t2 = 1):
    if r2 == 0:
        return s1, t1, r1
    q = r1// r2
    return EEA2(r2, r1-q*r2, \
                s2, s1-q*s2, \
                t2, t1-q*t2)


def inverse(m, a):
    _, b, _ = EEA(m, a)
    if b < 0:
        b += m
    return b


if __name__ == '__main__':
    #print(genPrime())
    #print(checkPrime(105))
    #print(modpow(5,2,7))
    #print(gcd(12, 8))
    
    a, b = 32, 7
    s, t, r = EEA(a, b)
    print('%d*%d + %d*%d = %d'%(a,s,b,t,r))
    print(inverse(a,b))
    
    
    
