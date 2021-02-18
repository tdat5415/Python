plain = 'test'

p = plain.encode('utf-8')

print(type(p))


s = [65,66,67,68]

print(bytes(s).decode('utf-8'))
