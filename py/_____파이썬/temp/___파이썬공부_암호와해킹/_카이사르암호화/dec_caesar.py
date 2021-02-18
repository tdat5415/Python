import _카이사르암호화 as cae

if __name__ == '__main__':
    h = open('enc.txt', 'rt')
    content = h.read()
    #print(content)
    h.close()

    content = cae.caesar(content, 'F', cae.DEC)
    content = content.lower()

    h = open('dec.txt', 'wt+')
    h.write(content)
    h.close()
    
