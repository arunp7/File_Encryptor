from cryptography.fernet import Fernet
input_file = input("Enter the file name: ")
output_file = "out.encrypted"
key = Fernet.generate_key()
file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()
with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)