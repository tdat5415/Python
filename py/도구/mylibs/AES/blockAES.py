from mylibs.AES import keyEx as kE
from mylibs.AES import sbox as sb
import numpy as np
import time as t


ENC = 1
DEC = 0

def AES_block(text, key, mod): #numpy array 4x4
    if mod == ENC:
        text =  block_enc(text, key)
    elif mod == DEC:
        text =  block_dec(text, key)
    else :
        return None
    
    return text


def block_enc(plain, key):#16바이트
    T = plain #numpy array 4x4
    K = kE.key_expantion(key) #numpy array 11x4x4 

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

    cipher = T
    
    return cipher


def block_dec(cipher, key):
    T = cipher #numpy array 4x4
    K = kE.key_expantion(key) #numpy array 11x4x4 

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

    decipher = T #np_block 4x4
    
    return decipher


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
    pass


    
