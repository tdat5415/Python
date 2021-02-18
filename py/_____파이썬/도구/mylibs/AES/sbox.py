ENC = 1
DEC = 0

def S_box(n, mod = ENC):
    if n > 0xff:
        print('Error in S_box')
        return None
    if mod == DEC:
        return inverse_S_box(n)
    
    b = EEA_sbox(0b100011011, n)#0b100011011
    B = [b>>i&1 for i in range(8)]
    S = [0]*8
    C = [1, 1, 0, 0, 0, 1, 1, 0]

    s = 0 
    for i in range(8):
        S[i] = B[i] ^ B[(i+4)%8] ^ B[(i+5)%8] ^ B[(i+6)%8] ^ B[(i+7)%8] ^ C[i]
        s += S[i]<<i

    return s


def inverse_S_box(s):
    S = [s>>i&1 for i in range(8)]
    B = [0]*8
    C = [1, 0, 1, 0, 0, 0, 0, 0]

    b = 0
    for i in range(8):
        B[i] = S[(i+2)%8] ^ S[(i+5)%8] ^ S[(i+7)%8] ^ C[i]
        b += B[i]<<i

    return EEA_sbox(0b100011011, b)


     
def EEA_sbox(r1, r2):#역원구하기비슷
    if r2 > 0xff:
        print('Error in EEA_sbox')
        return None
    if r2 == 0:
        return 0

    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 1:
        q, _ = bin_mod(r1, r2)#r1 // r2
        #print('q : ',bin(q))
        #print('r2 : ',hex(r2))
        #print('s2 : ',hex(s2))
        #print('t2 : ',hex(t2))
        r1, r2 = r2, r1 ^ bin_mul(q, r2, sbox = True)
        s1, s2 = s2, s1 ^ bin_mul(q, s2, sbox = True)
        t1, t2 = t2, t1 ^ bin_mul(q, t2, sbox = True)
    
    return t2

'''
def EEA_sbox2(r1, r2, \
             s1 = 1, s2 = 0, \
             t1 = 0, t2 = 1):#역원구하기비슷
    if r2 == 1:
        return t2
    elif r2 == 0:
        return 0
    q, _ = bin_mod(r1, r2)#r1 // r2
    
    return EEA_sbox(r2, r1 ^ bin_mul(q, r2), \
                    s2, s1 ^ bin_mul(q, s2), \
                    t2, t1 ^ bin_mul(q, t2))
'''

def bin_mod(a, b):#a%b  b가 a길이만큼 늘리고 쉬프트하면서 xor로 최고차항 뺌
    #Rijndael's finite field
    if a < b:
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

'''
def S_box2(n, inverse = False):
    if n > 0xff:
        print('Error in S_box2')
        return None
    if inverse == True:
        box = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]
        return box[n
                   ]
    box = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]
    return box[n]
'''


    
if __name__ == '__main__':
    #print(genPrime())
    #print(checkPrime(105))
    #print(modpow(5,2,7))
    #print(gcd(12, 8))
    a, b = 14, 9
    s, t, r = EEA2(a, b)
    print('%d*%d + %d*%d = %d'%(a,s,b,t,r))
    
    
