import sbox as sb
import numpy as np


def key_expantion(key, bit = 128):
    #128/192/256 -> 10/12/14라운드 -> 11/13/15개
    #key길이 : 16바이트
    if key >= 1<<128:
        print('Error in key_expantion')
        return None
    #w0~w3까지
    W = [0]*44 #4바이트가 44개
    for i in range(4):
        w = 0
        for j in range(32):
            w >>= 1
            if key & 1:
                w += 1<<31
            key >>= 1
        W[i] = w

    #w4~w43까지
    for i in range(4, 44):
        if i % 4 == 0:
            ron = (i-4)//4
            W[i] = W[i-4] ^ G_func(W[i-1], ron)
        else:
            W[i] = W[i-4] ^ W[i-1]
        
    #키로 만들기
    '''
    K = [] #16바이트가 11개
    for i in range(11):
        K.append([])
        for j in range(4):
            K[i].append([])
            w = W[4*i + j]#4바이트
            for k in range(4):
                one = w & 0xff
                w >>= 8
                K[i][j].append(one)
    '''
    K = [] #44x4 = 176
    for w in W:
        for i in range(4):
            one = w & 0xff
            w >>= 8
            K.append(one)
            
    K = np.array(K).reshape(11, 4, 4)
    
    return K # 11x4x4


def G_func(w, ron):
    if w > 0xffffffff:
        print('Error in G_func')
        return None
    w = rot_word(w)
    w = sub_word(w)
    w = xor_Rcon(w, ron)
    return w


def rot_word(w):
    s = w & 0xff000000
    w &= 0x00ffffff
    w <<= 8
    s >>= 24
    w |= s
    return w


def sub_word(w):
    for i in range(4):
        s = w & 0xff
        w >>= 8
        s = sb.S_box(s)
        w |= s<<24
    return w


def xor_Rcon(w, ron):
    Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
    return w ^ Rcon[ron]
    
    
                

if __name__ == '__main__':
    key = 0x01010101010101010101010101010101
    key = 0xf273649126349819283471029381AAAA
    
    
    print(hex(key),'\n')
    K = key_expantion(key)
