import _르그랑암호화 as rgr

if __name__ == '__main__':
    h = open('encryption.txt', 'rt')
    content = h.read()
    #print(content)
    h.close()

    encbook, decbook = rgr.makeCodeBook()
    content = rgr.decrypt(content, decbook)

    h = open('decryption.txt', 'wt+')
    h.write(content)
    h.close()
    
