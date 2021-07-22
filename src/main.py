#import packages
import os

try:
        from Crypto.PublicKey import RSA
except:
        print('pycryptodome not found')
        os.system('pip install pycryptodome')
        #clear
        os.system('reset')
        from Crypto.PublicKey import RSA

from Crypto.Cipher import PKCS1_OAEP
import binascii


#key generation


keyPair = RSA.generate(3072)


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
