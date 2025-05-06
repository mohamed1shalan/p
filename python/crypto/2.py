import secrets


def genrate_otp_key(length):
    return bytearray(secrets.randbits(8) for _ in range(length))


def encription(plantext, key):
    if len(key) < len(plantext):
        raise ValueError("OTP key must be at least as long as the plaintext")

    plantext = plantext.encode('utf-8')

    cipher_text = bytearray()
    for i in range(len(plantext)):
        cipher_text.append(plantext[i] ^ key[i])
    return cipher_text


def decryption(ciphertext, key):
    if len(key) < len(ciphertext):
        raise ValueError("OTP key must be at least as long as the ciphertext")
    plantext = bytearray()
    for i in range(len(ciphertext)):
        plantext.append(ciphertext[i] ^ key[i])
    return plantext.decode('utf-8')


my_message = "Mohamd Shalan"
print(f"Original message: {my_message}")
my_key = genrate_otp_key(20)
encription_masseg = encription(my_message, my_key)
print(f"Encripted message: {encription_masseg}")
decripted_masseg = decryption(encription_masseg, my_key)
print(f"Decripted message: {decripted_masseg}")
# print(f"Key: {key}")
