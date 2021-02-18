from mylibs.RSA import blockRSA as br
from mylibs.RSA import makeSystem as ms
from mylibs.math import mathFunc as mf
import random as rd
import numpy as np

MODE_ECB = 1
MODE_CBC = 2


def save_private_key():
    rsa_info = ms.make_RSA_system()
    with open('private_key.txt', 'w') as h:
        s = 'Decryption_key#%d#\n' %(rsa_info['D'])
        h.write(s)
        s = 'Field#%d#\n' %(rsa_info['N'])
        h.write(s)
        s = 'PHI#%d#\n' %(rsa_info['PHI'])
        h.write(s)


def import_system():
    with open('private_key.txt', 'r') as h:
        s1 = h.readline()
        s2 = h.readline()
        s3 = h.readline()

    D = int(s1.split('#')[1])
    N = int(s2.split('#')[1])
    PHI = int(s3.split('#')[1])
    
    private_key = (D, N, PHI)

    return private_key


def get_public_key(private_key):
    D = private_key[0]
    N = private_key[1]
    PHI = private_key[2]
    E = mf.inverse(PHI, D)

    public_key = (E,N)
    
    return public_key


def bytes_to_blocks(bytes_str):
    bytes_blocks = [] #32바이트씩
    bytes_blocks = np.array(list(bytes_str))
    bytes_blocks.reshape(
    






if __name__ == '__main__':
    save_private_key()
    private_key = import_system()
    public_key = get_public_key(private_key)

    msg = rd.randint(2, public_key[1])
    enc_msg = br.block_enc(msg, public_key)
    dec_msg = br.block_dec(enc_msg, private_key)
    print(msg)
    print()
    print(enc_msg)
    print()
    print(dec_msg)
    print()
    

    
