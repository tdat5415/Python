from mylibs.AES import sbox as sb
import numpy as np


def key_expantion(key, bit = 128): #numpy array 4x4
    #128/192/256 -> 10/12/14라운드 -> 11/13/15개
    #key길이 : 16바이트
    if type(key) is not np.ndarray:
        print('Error in key_expantion')
        return None
    
    #w0~w3까지
    W = [] #[0xff,0xff,0xff,0xff] 형태가 44개
    for i in range(4):
        W.append(key[i])
    
    #w4~w43까지
    for i in range(4, 44):
        if i % 4 == 0:
            ron = (i-4)//4
            w = W[i-4] ^ G_func(W[i-1], ron)
            W.append(w)
        else:
            w = W[i-4] ^ W[i-1]#numpy로 한번에 xor
            W.append(w)
        
    #키로 만들기
    K = [] #44x4 = 176
    for w in W:
        for i in range(4):
            K.append(w[i])
            
    K = np.array(K).reshape(11, 4, 4)
    
    return K # 11x4x4


def G_func(w, ron):#numpy array 4길이
    w = rot_word(w)
    w = sub_word(w)
    w = xor_Rcon(w, ron)
    
    return w


def rot_word(w):
    w[0], w[1], w[2], w[3] = w[3], w[0], w[1], w[2]
    
    return w


def sub_word(w):
    for i in range(4):
        w[i] = sb.S_box(w[i])
        
    return w


def xor_Rcon(w, ron):
    #RCon(Round Constant)는 4byte 값으로, 가장 오른쪽의 3byte는 모두 0이다.
    Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
    w[3] ^= Rcon[ron]
    
    return w
    
    
                

if __name__ == '__main__':
    '''
    key = np.array([0x01]*16).reshape(4,4)
    key = np.array([i for i in range(16)]).reshape(4,4)
    
    
    print(hex(key),'\n')
    K = key_expantion(key)
    '''
    pass
    
