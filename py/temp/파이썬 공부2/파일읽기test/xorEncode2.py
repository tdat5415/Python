import os

def _encode(n):
    return n ^ 0x41


file_list = os.listdir(".\\_plain")


for filename in file_list:
    with open('.\\_plain\\' + filename, "rb") as p:
        data = p.read()


    print(type(data))


    intdata = []
    for i in data:
        intdata.append(_encode(i))

    encodedata = []
    for i in intdata:
        encodedata.append(i)

    encodedata = bytes(encodedata)
    with open('.\\_encoded\\' + filename + '.enc', 'wb') as p:
        p.write(encodedata)


