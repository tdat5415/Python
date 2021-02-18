import __카이사르아핀암호화 as aff

if __name__ == '__main__':
    h = open('enc1.txt', 'rt')
    content = h.read()
    #print(content)
    h.close()

    content = aff.affine(content, 3, 5, aff.DEC)
    content = content.lower()

    h = open('dec1.txt', 'wt+')
    h.write(content)
    h.close()
    
