import _르그랑암호화 as rgr

if __name__ == '__main__':
    h = open('plain.txt', 'rt')
    content = h.read()
    #print(content)
    h.close()

    encbook, decbook = rgr.makeCodeBook()
    content = rgr.encrypt(content, encbook)

    h = open('encryption.txt', 'wt+')
    h.write(content)
    h.close()
    
