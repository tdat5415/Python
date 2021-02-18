from Crypto.Hash import SHA256 as SHA
SIZE = 1024*256 #256KB

def getFileHash(filename):
    hash = SHA.new()
    
    h = open(filename, 'rb')
    content = h.read(SIZE)
    
    hashval = b''
    while content:
        hash.update(content)  #btyes type 이 들어간다.
        hashval += hash.digest()  #32B 이어붙이기
        
        content = h.read(SIZE)
    h.close()
    
    hash.update(hashval)
    hashval = hash.digest()
    
    return hashval


def hashCheck(file1, file2):
    hashval1 = getFileHash(file1)
    hashval2 = getFileHash(file2)

    if hashval1 == hashval2:
        print('Two Files are Same')
    else :
        print('Two Files are Different')


def main():
    file1 = 'plain.txt'
    file2 = 'decipher.txt'
    hashCheck(file1, file2)


if __name__ == '__main__':
    main()
    
