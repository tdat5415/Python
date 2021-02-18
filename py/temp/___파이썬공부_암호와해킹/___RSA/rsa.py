from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as PO


def readPEM():
    with open('mykey.pem', 'rb') as h:
        s = h.read()
        #print(s)
        key = RSA.importKey(s)
    
    return key

def rsa_enc(msg):
    private_key = readPEM()
    public_key = private_key.publickey()
    
    #encdata = public_key.encrypt(msg, 32)
    encryptor = PO.new(public_key)
    encrypted = encryptor.encrypt(msg)

    return encrypted

def rsa_dec(msg):
    private_key = readPEM()
    
    #decdata = private_key.decrypt(msg)
    decryptor = PO.new(private_key)
    decrypted = decryptor.decrypt(msg)

    return decrypted


if __name__ == '__main__':
    msg = 'what the fuck is thatasdklfjhas;dfasdl;flaskfdja;sdklfja;sldfkas;ldfkjasdf;ljas;dlas;?'
    
    ciphered = rsa_enc(msg.encode('utf-8'))
    print(len(ciphered))
    print(ciphered)

    deciphered = rsa_dec(ciphered)
    print(len(deciphered))
    print(deciphered)

