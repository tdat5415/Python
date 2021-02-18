from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA
from Crypto.Signature import pkcs1_15 as p15

def readPEM():
    with open('mykey.pem', 'r') as h:
        key = RSA.importKey(h.read())

    return key

#사용자의 개인키로 서명하는 측
def rsa_sign(msg):
    private_key = readPEM()
    public_key = private_key.publickey()
    print(private_key)
    print(public_key)

    #hash = SHA.new(msg).digest()
    #signature = private_key.sign(hash, '')#개인키로 서명
    hash = SHA.new(msg)
    signature = p15.new(private_key).sign(hash) #개인키로 서명한 정보
    
    return public_key, signature

#사용자의 공개키로 서명을 확인하는 측
def rsa_verify(msg, public_key, signature):
    #hash = SHA.new(msg).digest()
    #if public_key.verify(hash, signature):#공개키로 확인
    #    print('VERIFIED')
    #else:
    #    print('DENIED')
    hash = SHA.new(msg)
    try:
        p15.new(public_key).verify(hash, signature)
        print('VERIFIED')
    except:
        print('DENIED')


if __name__ == '__main__':
    msg = 'what is that'
    public_key, signature = rsa_sign(msg.encode('utf-8'))
    print(type(public_key))
    rsa_verify(msg.encode('utf-8'), public_key, signature)
