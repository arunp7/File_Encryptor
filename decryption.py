#Import Modules From Cryptography
from cryptography.fernet import Fernet

#Enter the name of file that you want to decrypt
input_file = input("Enter the file name for decrypting: ")

#Name of the file that is decrypted
output_file = "decrypted.csv"

#Open and Read the key for encryption.
file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()

#Reading the input file for decryption
with open(input_file, 'rb') as f:
    data = f.read()
fernet = Fernet(key)
decrypted = fernet.decrypt(data)

#Writing the decrypted file to the output
with open(output_file, 'wb') as f:
    f.write(decrypted)
print("The file {} is decrypted successfully and saved as {}".format(input_file,output_file))