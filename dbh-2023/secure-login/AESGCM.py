#!/usr/bin/env python3
from Crypto.Cipher import AES

KEY    = "onequickbrownfox"
NONCE  = "somerandomstring"  # IV

def init_AES_GCM():
  return AES.new(key=KEY.encode(), mode=AES.MODE_GCM, nonce=NONCE.encode())


print("call of encrypt function:")

cipher = init_AES_GCM()
ciphertext = cipher.encrypt("admin1".encode())
print("ciphertext: " + ciphertext.hex())

print("\ncalls of decrypt function:")

cipher = init_AES_GCM()
plaintext = cipher.decrypt(ciphertext)

print("decrypt ciphertext: " + plaintext.decode())

cipher = init_AES_GCM()
plaintext = cipher.decrypt(ciphertext[:-1])

print("decrypt ciphertext[:-1]: " + plaintext.decode())



print("\n\ncall of encrypt_and_digest function:")

cipher = init_AES_GCM()
ciphertext, tag = cipher.encrypt_and_digest("admin1".encode())
print("ciphertext: " + ciphertext.hex())
print("tag: " + tag.hex())

print("\ncalls of decrypt_and_verify function:")

cipher = init_AES_GCM()
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print("decrypt ciphertext: " + plaintext.decode())

cipher = init_AES_GCM()
try:
    plaintext = cipher.decrypt_and_verify(ciphertext[:-1], tag)
    print("decrypt ciphertext[:-1]: " + plaintext.decode())
except ValueError as error:
    print("decrypt ciphertext[:-1]: ", end="")
    print(error)
    
    
