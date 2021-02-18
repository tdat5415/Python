from mylibs.math import mathFunc as mf
import random as rd

SIZE = 128


def make_RSA_system():
    t = 0
    for i in range(1000):
        p = mf.genPrime(SIZE) #128bit #16byte
        q = mf.genPrime(SIZE)
        if p*q > 1<<(SIZE+SIZE-1):#256bit맞출려고
            t = 1
            break
        #print('?')
    if t != 1:
        raise Exception('Failed to make field')

    N = p*q # 필드 N
    PHI = (p-1) * (q-1)

    for i in range(1000):
        E = rd.randint(2, PHI -1)
        t = mf.gcd(PHI, E)
        #print(t)
        if t == 1:
            break
    if t != 1:
        raise Exception('Failed to make encryption key')

    D = mf.inverse(PHI, E)
    #print('(E x D) % PHI = ', (E * D) % PHI)

    rsa_dict = {'E':E, 'D':D, 'N':N, 'PHI':PHI}
    return rsa_dict #encryption key, decryption key, field
    


if __name__ == '__main__':
    one = make_RSA_system()
    print('enc_key : \n', one['E'])
    print('dec_key : \n', one['D'])
    print('field : \n', one['N'])
    print('phi : \n', one['PHI'])

