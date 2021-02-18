import blockAES as bA

MODE_ECB = 1
MODE_CBC = 2

class AES():
    def __init__(self, key, op_mod, ivkey = 1234):
        self.int_key = block_str2int(key) #16바이트
        self.int_ivkey = block_str2int(ivkey) #16바이트
        self.op_mod = op_mod


    def encrypt(self, plaintext): #긴 텍스트 16배수 길이 #1024씩 들어올 예정
        if self.op_mod == MODE_ECB:
            text = self.encrypt_ecb(plaintext)
        elif self.op_mod == MODE_CBC:
            text = self.encrypt_cbc(plaintext)
        else :
            return None

        return text
    
    def encrypt_ecb(self, plaintext): # int_ivkey 필요없음
        plain_str_blocks = split_text(plaintext)
        plain_int_blocks = blocks_str2int(plain_str_blocks)

        cipher_int_blocks = []
        for plain_int_block in plain_int_blocks:
            cipher_int_block = bA.AES_block(plain_int_block, self.int_key, bA.ENC)
            cipher_int_blocks.append(cipher_int_block)

        cipher_str_blocks = blocks_int2str(cipher_int_blocks)
        ciphertext = concat_str_blocks(cipher_str_blocks)

        return ciphertext
        
    def encrypt_cbc(self, plaintext):
        plain_str_blocks = split_text(plaintext)
        plain_int_blocks = blocks_str2int(plain_str_blocks)

        cipher_int_blocks = []
        for i in range(len(plain_int_blocks)):
            cipher_int_block = plain_int_block[i]
            if i == 0:
                cipher_int_block ^= self.int_ivkey
            else :
                cipher_int_block ^= cipher_int_blocks[i-1]
            cipher_int_block = bA.AES_block(cipher_int_block, self.int_key, bA.ENC)
            cipher_int_blocks.append(cipher_int_block)
        
        cipher_str_blocks = blocks_int2str(cipher_int_blocks)
        ciphertext = concat_str_blocks(cipher_str_blocks)

        return ciphertext

    def decrypt(self, ciphertext): #긴 텍스트 16배수 길이 #1024씩 들어올 예정
        if self.op_mod == MODE_ECB:
            text = self.decrypt_ecb(ciphertext)
        elif self.op_mod == MODE_CBC:
            text = self.decrypt_cbc(ciphertext)
        else :
            return None

        return text

    def decrypt_ecb(self, ciphertext):
        cipher_str_blocks = split_text(ciphertext)
        cipher_int_blocks = blocks_str2int(cipher_str_blocks)

        decipher_int_blocks = []
        for cipher_int_block in cipher_int_blocks:
            decipher_int_block = bA.AES_block(cipher_int_block, self.int_key, bA.DEC)
            decipher_int_blocks.append(decipher_int_block)

        decipher_str_blocks = blocks_int2str(decipher_int_blocks)
        deciphertext = concat_str_blocks(decipher_str_blocks)

        return deciphertext

    def decrypt_cbc(self, ciphertext):
        cipher_str_blocks = split_text(ciphertext)
        cipher_int_blocks = blocks_str2int(cipher_str_blocks)

        decipher_int_blocks = []
        for i in range(len(cipher_int_blocks)):
            decipher_int_block = cipher_int_block[i]
            decipher_int_block = bA.AES_block(decipher_int_block, self.int_key, bA.DEC)
            if i == 0:
                decipher_int_block ^= self.int_ivkey
            else :
                decipher_int_block ^= cipher_int_blocks[i-1]
            
            decipher_int_blocks.append(decipher_int_block)
        
        decipher_str_blocks = blocks_int2str(decipher_int_blocks)
        deciphertext = concat_str_blocks(decipher_str_blocks)

        return deciphertext
        
    
    
def split_text(text):
    if len(text)%16 != 0:
        raise Exception('Error in split_text')

    block_len = len(text)//16
    text_blocks = []
    for i in range(block_len):
        block = text[i*16:(i+1)*16]
        text_blocks.append(block)

    return text_blocks

def concat_str_blocks(str_blocks):
    text = ''
    for str_block in str_blocks:
        text += str_block

    return text

def blocks_str2int(str_blocks):
    int_blocks = []
    for str_block in str_blocks:
        int_block = block_str2int(str_block)
        int_blocks.append(int_block)

    return int_blocks

def block_str2int(str_block):
    if len(str_block) != 16:
        raise Exception('Error in block_str2int')
        
    int_block = 0
    for i in range(16):
        int_block |= ord(str_block[i])<<i*8

    return int_block
        
def blocks_int2str(int_blocks):
    str_blocks = []
    for int_block in int_blocks:
        str_block = block_int2str(int_block)
        str_blocks.append(str_block)

    return str_blocks

def block_int2str(int_block):
    if int_block >= 1<<128:
        raise Exception('Error in block_int2str')

    str_block = ''
    for i in range(16):
        str_block += chr(0xff & int_block)
        int_block >>= 8

    return str_block
    

if __name__ == '__main__':
    str_blocks = split_text('asdfqwerzxcvasdfjhgfuytrmnbvpoiu')
    text = concat_str_blocks(str_blocks)
    print(text)

    aes = AES('jhgfuytrmnbvpoiu', MODE_ECB, 'jhgfuytrmnbvpoiu')
    
    cipher = aes.encrypt(text)
    print(cipher)

    decipher = aes.decrypt(cipher)
    print(decipher)

    
        
