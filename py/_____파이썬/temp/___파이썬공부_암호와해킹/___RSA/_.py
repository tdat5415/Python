from Crypto.Hash import SHA256 as SHA


msg = b'test'
#hash = SHA.new(msg).digest()
hash = SHA.new(msg)

print(hash)
