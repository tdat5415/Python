from Crypto.Hash import SHA256 as SHA

SIZE = 16

def xorECB_enc(msg, key):
    msg_arr = edit_msg(msg)#[n][16]
    key_16 = edit_key(key)#[16]

    msg_arr_xor = []
    
    for line in msg_arr:
        tmp = xorCel(line, key_16)#[16]
        msg_arr_xor.append(tmp)

    remake_msg = b''
    for line in msg_arr_xor:
        #for v in line:
        #    remake_msg += chr(v)
        remake_msg += line

    return remake_msg


def edit_msg(msg):
    zeros = SIZE - len(msg)%SIZE

    head = str(zeros)
    _nums = SIZE - len(head)%SIZE
    head += '_'*_nums

    msg += '0'*zeros
    msg = head + msg
    print(msg)

    msg = msg.encode('utf-8')

    return reshape_arr(msg)


def reshape_arr(msg):
    msg_len = len(msg)
    blocks_num = msg_len//SIZE
    
    msg_arr = []
    for i in range(blocks_num):
        msg_arr.append(msg[:SIZE])
        msg = msg[SIZE:]

    print(msg_arr)
    return msg_arr


def edit_key(key):
    hash = SHA.new()
    hash.update(key.encode('utf-8'))
    k = hash.digest()
    return k[:SIZE]


def xorCel(line ,k):
    block = []
    for i in range(SIZE):
        block.append(line[i]^k[i])
    return bytes(block)


def xorECB_dec(msg,key):
    pass
    key_16 = edit_key(key)#[16]
    msg_arr = reshape_arr(msg)#[n][16]
    
    for i in range(len(msg_arr)):
        msg_arr[i] = xorCel(msg_arr[i], key_16).decode('utf-8')

    zeros = int(msg_arr[0].split('_')[0])
    msg_arr[-1] = msg_arr[-1][:SIZE-zeros]

    remake_msg = ''
    for line in msg_arr[1:]:
        remake_msg += line

    return remake_msg


if __name__ == '__main__':
    msg = 'this is super mega ultra test'
    key = 'test'

    enc_msg = xorECB_enc(msg,key)#바이트스트림
    print(enc_msg)
    print(len(enc_msg))

    dec_msg = xorECB_dec(enc_msg,key)
    print(dec_msg)

    
