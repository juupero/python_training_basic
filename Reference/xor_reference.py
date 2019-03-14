def xor_encrypt(message, key):
    return ''.join(
        chr(ord(char) ^ ord(key[i % len(key)]))
        for i, char in enumerate(message)
    )


def xor_decrypt(message, key):
    return xor_encrypt(message, key)
