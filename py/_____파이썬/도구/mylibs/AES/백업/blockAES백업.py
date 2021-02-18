import keyEx as kE
import numpy as np
import sbox as sb
import time as t


ENC = 1
DEC = 0

def AES_block(text, key, mod):
    if mod == ENC:
        text =  block_enc(text, key)
    elif mod == DEC:
        text =  block_dec(text, key)
    else :
        return None
    
    return text


def block_enc(plain, key):#16바이트
    T = change_blockto4x4(plain) #4x4
    K = kE.key_expantion(key) #11x4x4

    #처음
    T = add_round_key(T, K[0])
    
    #1~9라운드
    for i in range(1, 10):
        T = sub_byte(T)
        T = shift_row(T)
        T = mix_column(T)
        T = add_round_key(T,K[i])

    #10라운드
    T = sub_byte(T)
    T = shift_row(T)
    T = add_round_key(T,K[10])

    cipher = change_4x4toblock(T)
    
    return cipher


def block_dec(cipher, key):
    T = change_blockto4x4(cipher) #4x4
    K = kE.key_expantion(key) #11x4x4

    #처음
    T = add_round_key(T, K[10])

    #1~9라운드
    for i in range(9,0,-1):
        T = shift_row(T, mod = DEC)
        T = sub_byte(T, mod = DEC)
        T = add_round_key(T,K[i])
        T = mix_column(T, mod = DEC)

    #10라운드
    T = shift_row(T, mod = DEC)
    T = sub_byte(T, mod = DEC)
    T = add_round_key(T,K[0])

    decipher = change_4x4toblock(T)
    
    return decipher

    
def change_blockto4x4(text):
    T = []
    for i in range(16):
        one = text & 0xff
        text >>= 8
        T.append(one)
        
    T = np.array(T).reshape(4, 4)
    
    return T


def change_4x4toblock(T):
    text = 0
    T = T.reshape(16)
    for i in range(16):
        t = int(T[i])
        text |= t<<(i*8)
        
    return text


def add_round_key(T, K):
    return T ^ K


def sub_byte(T, mod = ENC):#4x4
    T = T.reshape(16)
    T = np.array(list(map(sb.S_box,T,[mod]*16)))
    T = T.reshape(4,4)
    
    return T


def shift_row(T, mod = ENC):
    if mod == ENC:
        T[1] = np.array([T[1][(i+1)%4] for i in range(4)])
        T[2] = np.array([T[2][(i+2)%4] for i in range(4)])
        T[3] = np.array([T[3][(i+3)%4] for i in range(4)])
    elif mod == DEC:
        T[1] = np.array([T[1][(i-1)%4] for i in range(4)])
        T[2] = np.array([T[2][(i-2)%4] for i in range(4)])
        T[3] = np.array([T[3][(i-3)%4] for i in range(4)])
        
    return T


def mix_column(T, mod = ENC):
    if mod == ENC:
        M = [[2,3,1,1],
             [1,2,3,1],
             [1,1,2,3],
             [3,1,1,2]]
    elif mod == DEC:
        M = [[14,11,13,9],
             [9,14,11,13],
             [13,9,14,11],
             [11,13,9,14]]
    M = np.array(M)
    
    T = T.T
    
    X = np.full((4,4),0)
    for i in range(4):
        for j in range(4):
            Y = list(map(sb.bin_mul,M[j],T[i]))
            X[j][i] = Y[0] ^ Y[1] ^ Y[2] ^ Y[3]
        
    return X
    


if __name__ == '__main__':
    K = 0xafafafaf1212121256565656c5c6c7c8#block
    T1 = 0x10238947109587195871023489710235
    T2 = 0x19238471902385601928365123509817

    A = np.array([[0x87, 0xf2, 0x4d, 0x97],
                  [0x6e, 0x4c, 0x90, 0xec],
                  [0x46, 0xe7, 0x4a, 0xc3],
                  [0xa6, 0x8c, 0xd8, 0x95]])
    '''
    print(A)
    print()
    B = shift_row(A)
    print(B)
    print()
    A = shift_row(B,mod = DEC)
    print(A)
    print()
    '''
    
    '''
    print(hex(T))
    
    t1 = t.time()
    C = AES_block(T, K, ENC)
    t2 = t.time()
    print('걸린시간 : %f' % (t2-t1))
    print(hex(C))

    t1 = t.time()
    D = AES_block(C, K, DEC)
    t2 = t.time()
    print('걸린시간 : %f' % (t2-t1))
    print(hex(D))
    '''
    
    C = AES_block(T1^T2, K, ENC)
    print(hex(C))

    C = AES_block(T1, K, ENC) ^ AES_block(T2, K, ENC)
    print(hex(C))


    
