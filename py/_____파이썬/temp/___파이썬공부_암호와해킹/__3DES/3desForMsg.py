from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA


class myDES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:24]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:8]


    def enc(self, plaintext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        encmsg = des3.encrypt(plaintext.encode())
        return encmsg


    def dec(self, ciphertext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        decmsg = des3.decrypt(ciphertext)
        return decmsg


def main():
    keytext = 'samsjang'
    ivtext = '1234'
    msg = 'python35ab'

    myCipher = myDES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)
    print('plain : \t', msg)
    print('ciphered : \t', ciphered)
    print('decipherd : \t', deciphered)

if __name__ == '__main__':
    main()
    

