from mylibs.AES import blockAES as bA
import numpy as np

MODE_ECB = 1
MODE_CBC = 2

class AES():
    def __init__(self, key_bytes, op_mod, ivkey_bytes = None): #bytes 타입의 key가 들어온다.
        self.key_np_block = np.array(list(key_bytes)).reshape(4,4) #4x4 numpy array로 바꾼다
        self.ivkey_np_block = None
        if ivkey_bytes != None:
            self.ivkey_np_block = np.array(list(ivkey_bytes)).reshape(4,4)
        self.op_mod = op_mod


    def encrypt(self, plain_bytes): #긴 bytes 16배수 길이 #1024씩 들어올 예정
        if self.op_mod == MODE_ECB:
            cipher_bytes = self.encrypt_ecb(plain_bytes)
        elif self.op_mod == MODE_CBC:
            cipher_bytes = self.encrypt_cbc(plain_bytes)
        else :
            return None

        return cipher_bytes
    
    def encrypt_ecb(self, plain_bytes): #긴 bytes 16배수 길이 # int_ivkey 필요없음
        plain_np_blocks = long_bytes_to_np_blocks(plain_bytes)

        cipher_np_blocks = []
        for plain_np_block in plain_np_blocks:
            cipher_np_block = bA.AES_block(plain_np_block, self.int_np_block, bA.ENC)
            cipher_np_blocks.append(cipher_np_block)
        cipher_np_blocks = np.array(cipher_np_blocks)

        cipher_bytes = np_blocks_to_bytes(cipher_np_blocks)

        return cipher_bytes #긴 bytes 16배수 길이
        
    def encrypt_cbc(self, plain_bytes):
        plain_np_blocks = long_bytes_to_np_blocks(plain_bytes)

        cipher_np_blocks = []
        for i in range(len(plain_np_blocks)):
            cipher_np_block = plain_np_blocks[i]
            if i == 0:
                cipher_np_block ^= self.ivkey_np_block #np array로 한번에
            else :
                cipher_np_block ^= cipher_np_blocks[i-1]
            cipher_np_block = bA.AES_block(cipher_np_block, self.key_np_block, bA.ENC)
            cipher_np_blocks.append(cipher_np_block)
        cipher_np_blocks = np.array(cipher_np_blocks)
        
        cipher_bytes = np_blocks_to_bytes(cipher_np_blocks)

        return cipher_bytes

    def decrypt(self, cipher_bytes): #긴 텍스트 16배수 길이 #1024씩 들어올 예정
        if self.op_mod == MODE_ECB:
            decipher_bytes = self.decrypt_ecb(cipher_bytes)
        elif self.op_mod == MODE_CBC:
            decipher_bytes = self.decrypt_cbc(cipher_bytes)
        else :
            return None

        return decipher_bytes

    def decrypt_ecb(self, cipher_bytes):
        cipher_np_blocks = long_bytes_to_np_blocks(cipher_bytes)

        decipher_np_blocks = []
        for cipher_np_block in cipher_np_blocks:
            decipher_np_block = bA.AES_block(cipher_np_block, self.key_np_block, bA.DEC)
            decipher_np_blocks.append(decipher_np_block)
        decipher_np_blocks = np.array(decipher_np_blocks)

        decipher_bytes = np_blocks_to_bytes(decipher_np_blocks)

        return decipher_bytes

    def decrypt_cbc(self, cipher_bytes):
        cipher_np_blocks = long_bytes_to_np_blocks(cipher_bytes)

        decipher_np_blocks = []
        for i in range(len(cipher_np_blocks)):
            decipher_np_block = cipher_np_blocks[i]
            decipher_np_block = bA.AES_block(decipher_np_block, self.key_np_block, bA.DEC)
            if i == 0:
                decipher_np_block ^= self.ivkey_np_block
            else :
                decipher_np_block ^= cipher_np_blocks[i-1]
            
            decipher_np_blocks.append(decipher_np_block)
        decipher_np_blocks = np.array(decipher_np_blocks)
        
        decipher_bytes = np_blocks_to_bytes(decipher_np_blocks)

        return decipher_bytes
        
    
def long_bytes_to_np_blocks(long_bytes):
    if len(long_bytes) % 16 != 0:
        raise Exception('Error in long_bytes_to_np_blocks')
    blocks_num = len(long_bytes) // 16
    np_blocks = np.array(list(long_bytes)).reshape(blocks_num,4,4)

    return np_blocks

def np_blocks_to_bytes(np_blocks):
    blocks_num = len(np_blocks)

    return bytes(list(np_blocks.reshape(blocks_num * 16)))

def new(key_bytes, op_mod, ivkey_bytes = None):
    return AES(key_bytes, op_mod, ivkey_bytes)

if __name__ == '__main__':
    pass

    
        
