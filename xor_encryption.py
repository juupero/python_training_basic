def xor_encrypt(text, key):
  key_character = 0
  encrypted_text = ""
  for char in text:
    if key_character == len(key) - 1:
      key_character = 0
    if char is " ":
      encrypted_text += " "
      continue
    encrypted_text += chr(ord(char) + ord(key[key_character]))
    key_character += 1
  return encrypted_text

def xor_decrypt(secret_text, key):
  key_character = 0
  decrypted_text = ""
  for char in secret_text:
    if key_character == len(key) - 1:
      key_character = 0
    if char is " ":
      decrypted_text += " "
      continue
    decrypted_text += chr(ord(char) - ord(key[key_character]))
    key_character += 1
  return decrypted_text

print(xor_encrypt("I am a little teapot", "china"))
print(xor_decrypt("¬ ÉÖ Ï ÏÑÝâÏÍ ÝÓÄØØâ", "china"))
