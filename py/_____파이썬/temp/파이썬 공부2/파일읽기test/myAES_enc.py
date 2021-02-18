from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
from os import path
import os

KSIZE = 1024

class _AES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:16]

    def makeEncInfo(self, filename):
        fillersize = 0
        filesize = path.getsize(filename)

        if filesize%16 != 0:
            fillersize = 16 - filesize%16

        filler = '0' * fillersize
        header = '%d' % (fillersize)
        gap = 16 - len(header)
        header += '#' * gap

        return header, filler

    def enc(self, filename):
        encfilename = '.\\_encoded\\' + filename + '.enc'
        filename = '.\\_plain\\' + filename
        
        header, filler = self.makeEncInfo(filename)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)

        h = open(filename, 'rb')
        hh = open(encfilename, 'wb+')

        enc = header.encode('utf-8')
        content = h.read(KSIZE)
        content = enc + content

        while content:
            if len(content) < KSIZE:
                content += filler.encode('utf-8')
            enc = aes.encrypt(content)
            hh.write(enc)
            content = h.read(KSIZE)

        h.close()
        hh.close()

def main():
    keytext = 'tdat'
    ivtext = 'tdat'
    
    myCipher = _AES(keytext, ivtext)

    file_list = os.listdir(".\\_plain")
    
    for filename in file_list:
        myCipher.enc(filename)

    

if __name__ == '__main__':
    main()
        




        
