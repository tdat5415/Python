import math


def fac(n):
    if type(n) is not int:
        raise Exception('insert integer')
    if n <= 1:
        return 1
    return n * fac(n-1)


def nCr(n, r):
    return fac(n) / (fac(n-r)*fac(r))


def nHr(n, r):
    return nCr(n+r-1, r)


def nPr(n, r):
    return fac(n) / fac(n-r)







def main():
    
    r = 23
    #res = 1 - nCr(365, r) / nHr(365, r) # 1 - (생일이 겹치지 않을 확률)
    res = 1 - nPr(365, 23)/(365**r)
    print(res)
    
    '''
    n = 23
    res = 1 - fac(365)/((365**n) * fac(365-n))
    print(res)
    '''


if __name__ == '__main__':
    main()
