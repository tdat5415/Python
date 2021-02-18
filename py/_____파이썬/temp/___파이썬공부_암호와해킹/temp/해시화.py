from Crypto.Hash import SHA256 as SHA

key = 'test'

hash = SHA.new()
hash.update(key.encode('utf-8')) # key를 utf-8방식으로 바이트스트림으로 변환
k = hash.digest()

print(key)
print(k)

for c in k:
    print(chr(c), end='')
