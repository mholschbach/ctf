import string
import random

ALPHABET = string.ascii_uppercase


def generate_key():
    #return [random.randint(0, 26) for _ in range(13)]
    return [ 14, 5, 18, 7, 18, 18, 7, 3, 11, 14, 1, 10, 14]

def generate_keystream(key, length):
    keystream = []
    while len(keystream) < length:
        keystream.extend(key)
        key = key[1:] + key[:1]
    return keystream


def encrypt(message, key):
    indices = [ALPHABET.index(c) if c in ALPHABET else c for c in message.upper()]
    keystream = generate_keystream(key, len(message))
    encrypted = []

    for i in range(len(indices)):
        if isinstance(indices[i], int):
            encrypted.append(ALPHABET[(keystream[i] + indices[i]) % 26])
        else:
            encrypted.append(indices[i])

    return "".join(encrypted)


#with open("plaintext.txt", "r") as f:
with open("ciphertext.txt", "r") as f:
    plaintext = f.read()

key = generate_key()
print("key: " + str(key))
ciphertext = encrypt(plaintext, key)
print("plaintext:\n" + str(ciphertext))


#with open("ciphertext.txt", "w") as f:
#    f.write(ciphertext)
