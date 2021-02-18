import os

def _decode(n):
    return n ^ 0x41


file_list = os.listdir(".\\_encoded")


for filename in file_list:
    words = filename.split('.')
    del(words[-1])
    filename = '.'.join(words)

    
    with open('.\\_encoded\\' + filename + '.enc', "rb") as p:
        data = p.read()


    print(type(data))


    intdata = []
    for i in data:
        intdata.append(_decode(i))

    encodedata = []
    for i in intdata:
        encodedata.append(i)

    encodedata = bytes(encodedata)
    with open('.\\_decoded\\' + filename, 'wb') as p:
        p.write(encodedata)


