#import packages
import os, sys

try:
        from Crypto.PublicKey import RSA
except:
        print('pycryptodome not found')
        os.system('pip install pycryptodome')
        #clear
        os.system('reset')
        from Crypto.PublicKey import RSA

import Crypto.Random
from Crypto.Cipher import PKCS1_OAEP
import binascii


#key generation
randomByte = Crypto.Random.get_random_bytes(191)
print(type(randomByte), randomByte)
print("\n")
byteToInt = int.from_bytes(randomByte, "big")
print(byteToInt)
print("\n")
print(byteToInt.to_bytes(sys.getsizeof(byteToInt), 'little'))


def fakerandfunc(n):
        print(n, "\n")
        get = Crypto.Random.get_random_bytes(n)
        print(get, "\n\n")
        return get

""""
keyPair = RSA.generate(3072, randfunc=fakerandfunc)


pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))




#encryption
msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))



#decrpytion
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)


#source world wide web cryptobook.nakov.com

"""
