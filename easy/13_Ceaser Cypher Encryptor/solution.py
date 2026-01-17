def caesarCipherEncryptor(string, key):
    encrypted_list = list()

    for char in string:
        encrypted_char = chr((ord(char)-ord('a')+key)%26 + ord('a'))
        encrypted_list.append(encrypted_char)
    return "".join(encrypted_list)