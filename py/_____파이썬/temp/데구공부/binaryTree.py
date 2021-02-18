

class _BT():
    lchild = None
    rchild = None
    data = None
    def __init__(self):
        pass
        
    #return True or False
    def isEmpty(self):
        if self.lchild == None and self.rchild == None:
            return True
        else :
            return False

def getDepth(T, d, maxd):
    if d > maxd:
        maxd = d
    if T.lchild != None:
        maxd = getDepth(T.lchild, d+1, maxd)
    if T.rchild != None:
        maxd = getDepth(T.rchild, d+1, maxd)
    return maxd
    

def isEqual(T1, T2):
    if not(T1 == None or T2 == None) and T1.data == T2.data:
        return isEqual(T1.lchild, T2.lchild) and isEqual(T1.rchild, T2.rchild)
    elif T1 == None and T2 == None:
        return True
    else :
        return False


def main():
    A = _BT()
    A.data = '가'
    
    B = A.lchild = _BT()
    C = A.rchild = _BT()
    B.data = '나'
    C.data = '다'

    D = B.lchild = _BT()
    D.data = '라'

    print(getDepth(A, 1, 1))

    print(isEqual(A,A))

    

if __name__ == '__main__':
    main()
