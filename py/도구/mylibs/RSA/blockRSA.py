from mylibs.RSA import makeSystem as ms
from mylibs.math import mathFunc as mf
import random as rd

def block_enc(msg_int, public_key): #int #2**128
    enc_key = public_key[0]
    field = public_key[1]
    
    if msg_int >= field:
        raise Exception('msg is big!!')
    
    return mf.modpow(msg_int, enc_key, field)


def block_dec(enc_msg_int, private_key):
    dec_key = private_key[0]
    field = private_key[1]
    
    if enc_msg_int >= field:
        raise Exception('enc_msg is big!!')
    
    return mf.modpow(enc_msg_int, dec_key, field)


if __name__ == '__main__':
    rsa_info = ms.make_RSA_system()
    
    msg = rd.randint(2, rsa_info['N']-1)
    enc_msg = block_enc(msg, (rsa_info['E'], rsa_info['N']))
    dec_msg = block_dec(enc_msg, (rsa_info['D'], rsa_info['N']))
    print(msg)
    print()
    print(enc_msg)
    print()
    print(dec_msg)
