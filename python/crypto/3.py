# Function to generate a key with the same length as the message
def generate_key(msg, key):
    key = list(key.upper())
    if len(msg) == len(key):
        return ''.join(key)
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

# Function to encrypt the message using Vigenère cipher


def encrypt_vigenere(msg, key):
    msg = msg.upper()
    key = generate_key(msg, key)
    cipher_text = []
    for i in range(len(msg)):
        x = (ord(msg[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ''.join(cipher_text)

# Function to decrypt the encrypted message


def decrypt_vigenere(msg, key):
    msg = msg.upper()
    key = generate_key(msg, key)
    orig_text = []
    for i in range(len(msg)):
        x = (ord(msg[i]) - ord(key[i])) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ''.join(orig_text)


message = "HELLO"
keyword = "KEY"

encrypted = encrypt_vigenere(message, keyword)
print("Encrypted:", encrypted)

decrypted = decrypt_vigenere(encrypted, keyword)
print("Decrypted:", decrypted)
