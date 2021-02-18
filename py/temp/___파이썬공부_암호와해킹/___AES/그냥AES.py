from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
import time as t


class myAES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:16]


    def makeEnabled(self, plaintext):
        fillersize = 0
        textsize = len(plaintext)
        
        fillersize = 16 - textsize%16

        filler = '0' * fillersize
        header = '%d' %(fillersize)
        gap = 16 - len(header)
        header += '#' * gap

        return header + plaintext + filler


    def enc(self, plaintext):
        plaintext = self.makeEnabled(plaintext)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        encmsg = aes.encrypt(plaintext.encode())
        return encmsg

    def dec(self, ciphertext):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decmsg = aes.decrypt(ciphertext)

        header = decmsg[:16].decode()
        fillersize = int(header.split('#')[0])
        if fillersize != 0:
            decmsg = decmsg[16:-fillersize]
        else:
            decmsg = decmsg[16:]
        return decmsg.decode()


def main():
    key = 'tdat'
    ivkey = 'what'
    plain = 'abcdefghijklmno'

    t1 = t.time()
    for i in range(100):
        aes = myAES(key, ivkey)
        cipher = aes.enc(plain)
        decipher = aes.dec(cipher)
    t2 = t.time()

    print('time : \t', t2-t1)
    print('plain : \t', plain)
    print('cipher : \t', cipher)
    print('decipher : \t', decipher)
    

if __name__ == '__main__':
    main()
    
