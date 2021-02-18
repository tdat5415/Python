from Crypto.Hash import SHA256 as SHA

hash = SHA.new()
hash.update(b'test')
hashval = hash.digest()
print(hashval)
