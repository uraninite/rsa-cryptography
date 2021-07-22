  
import hashlib
  
# initializing string
str = "TOKENAUTHNLX"
  
# encoding GeeksforGeeks using encode()
# then sending to SHA256()
token = hashlib.sha512(str.encode())


def modrandfunc(token, n):
        n+=n
        token = token.digest().hex()
 
        if (len(token) < n):
                j = n - 128
                
                longByte = ""

                while (len(longByte) <= n):
                        longByte+=token
                
                #modrandfunc(token, )
                
                print(j, n)
        


                return longByte[:n]
        elif (len(token) == n): 
                return token
        else:
                return token[:n]

print(modrandfunc(token, 500))

print("\n")

# printing the equivalent hexadecimal value.
print("The binary equivalent of SHA256 is :")

print("\n")


print(bytes.fromhex(modrandfunc(token, 191)))

print("\n")

print(token.digest())

print("\n")

print(token.digest().hex())

print("\n")

print(bytes.fromhex(token.digest().hex()))

print("\n")

print(token.digest().hex()[:2])

