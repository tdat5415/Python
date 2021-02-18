hel = '안녕하세요?'#한글은 3바이트쓰네
print(len(hel))
length = len(hel.encode('utf-8'))
print(length)

hel = 'Hello?'
print(len(hel))
length = len(hel.encode('utf-8'))
print(length)
