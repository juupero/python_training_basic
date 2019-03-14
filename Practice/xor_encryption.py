def xor_encrypt(text, key):
  key_character = 0
  encrypted_text = ""
  for char in text:
    if key_character == len(key) - 1:
      key_character = 0
    if char is " ":
      encrypted_text += " "
      continue
    encrypted_text += chr(ord(char) ^ ord(key[key_character]))
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

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]


def xor_crypt(text, key):
    expanded_key = repeat_to_length(key, len(text))
    index = 0
    encrypted_string = ""
    for char in text:
        original_char_ascii = ord(char)
        key_char_ascii = ord(expanded_key[index:index+1])
        shifted_char = chr(original_char_ascii ^ key_char_ascii)
        encrypted_string += shifted_char
        index = index + 1

    return encrypted_string


def xor_encrypt2(text, key):
    return xor_crypt(text, key)


def xor_decrypt2(secret_text, key):
    return xor_crypt(secret_text, key)


print(xor_encrypt("Thisisasecretmessage!", "china"))  # QBVVU
print(xor_decrypt("QBVVU", "asde"))  # 01234

# print(xor_encrypt2("Iamalittleteapot", "china"))
# print(xor_decrypt2("¬ ÉÖ Ï ÏÑÝâÏÍ ÝÓÄØØâ", "china"))
