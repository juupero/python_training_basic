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
  encrypted_msg = ""
  for char in msg:
    modulo_amount = (ALPHABET.index(char) + shift) % len(ALPHABET)
    encrypted_msg += ALPHABET[modulo_amount]
  return encrypted_msg


def decrypt(encrypted_msg, shift):
  """
  Takes string encrypted_msg and an integer shift
  returns new string which is a decrypted version
  of the message
  str, int -> str
  print(decrypt('eDUHM', 25)) -> Kevin
  print(decrypt('j.GT', -10000)) -> Ivan
  """
  msg = ""
  for char in encrypted_msg:
    modulo_amount = (ALPHABET.index(char) - shift) % len(ALPHABET)
    msg += ALPHABET[modulo_amount]
  return msg

# Results
print(encrypt('John', 15)) # 'YDwC'
print(encrypt(' ', 6)) # 'b'
print(decrypt('eDUHM', 25)) # Kevin
print(decrypt('j.GT', -10000)) # Ivan