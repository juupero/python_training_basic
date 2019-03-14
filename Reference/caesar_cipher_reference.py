# DO NOT MODIFY THESE 2 LINES
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET += ALPHABET.upper() + ' .,!?'


def encrypt(msg, shift):
    """
    Takes string msg and an integer shift
    returns new string which is an encrypted version
    of the message
    str, int -> str
    print(encrypt('John', 15)) -> 'YDwC'
    print(encrypt(' ', 6)) -> 'b'
    """
    return ''.join(
        ALPHABET[(ALPHABET.index(letter) + shift) % len(ALPHABET)]
        for letter in msg
    )

def decrypt(encrypted_msg, shift):
    """
    Takes string encrypted_msg and an integer shift
    returns new string which is a decrypted version
    of the message
    str, int -> str
    print(decrypt('eDUHM', 25)) -> Kevin
    print(decrypt('j.GT', -10000)) -> Ivan
    """
    return encrypt(encrypted_msg, -shift)
