#Import Modules From Cryptography
from cryptography.fernet import Fernet

#Enter the name of file that you want to encrypt
input_file = input("Enter the file name: ")

#Encrypted file will be saved as out.encryted
output_file = "out.encrypted"

#Key generation for Encryption
key = Fernet.generate_key()

#Key is saved in a file called "key.key" 
#Only if you have this key you will be able to decrypt the file
file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()

#Reading the input file
with open(input_file, 'rb') as f:
    data = f.read()

#Encryption using the key
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Generating the output(Encrypted) File
with open(output_file, 'wb') as f:
    f.write(encrypted)
