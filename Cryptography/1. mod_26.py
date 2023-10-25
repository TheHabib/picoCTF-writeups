import codecs

def decrypt_rot13(text):
    return codecs.decode(text, 'rot_13')


# Example usage:
encrypted_message = input("Enter ROT13 Message: ")
print(f"Decrypted Message: {decrypt_rot13(encrypted_message)}")