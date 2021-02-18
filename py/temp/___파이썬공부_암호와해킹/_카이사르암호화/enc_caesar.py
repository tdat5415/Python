import _카이사르암호화 as cae

if __name__ == '__main__':
    h = open('plain.txt', 'rt')
    content = h.read()
    #print(content)
    h.close()

    content = cae.caesar(content, 'F', cae.ENC)
    content = content.lower()

    h = open('enc.txt', 'wt+')
    h.write(content)
    h.close()
    
