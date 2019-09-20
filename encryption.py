
def encryptor(file_name):
        #Imports 
        from cryptography.fernet import Fernet
        import os.path

        #Enter the name of file that you want to encrypt
        input_file = file_name

        try:        
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
            print("The file {} is encrypted successfully and saved as {}".format(input_file,output_file))
            print("\n Please keep the value of key from file key.key file secure for decryption of the same in future.")

        #Handling error if the file does not exist.
        except Exception:
            print("{} does not exist in the current directory. Please enter a valid a file name.".format(file_name))
