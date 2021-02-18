with open("aaa.py", "rb") as p:
    data = p.read()


print(type(data))


intdata = []
for i in data:
    intdata.append(i ^ 0x41)

encodedata = []
for i in intdata:
    encodedata.append(i)

encodedata = bytes(encodedata)
with open("encoded.py", 'wb') as p:
    p.write(encodedata)


