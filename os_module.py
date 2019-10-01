import os
# let's create a module to encrypt and decrypt a file

# print(os.getcwd()) prints out directory

def encrypt(file):
    encoded_file = os.fsencode(file)
    return encoded_file
    # encrypt some file
    # return said encrypted file

def decrypt(file):
    decoded_file = os.fsdecode(file)
    return decoded_file
    # decrypt file
    # return said decrypted file
