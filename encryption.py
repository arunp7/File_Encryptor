
def encryptor(file_name):
        #Imports 
        from cryptography.fernet import Fernet
        import os

        #Input
        input_file = file_name
        try:
            if os.path.isfile(input_file):
                            
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
                print("PLEASE KEEP THE VALUE OF KEY FROM FILE key.key FILE AND SECURE IT FOR DECRYPTION OF THE SAME IN FUTURE.")
            else:
                raise FileNotFoundError
        
        #Handling error if the file does not exist.
        except FileNotFoundError:
            print("{} does not exist in the current directory. Please enter a valid a file name.".format(file_name))
        except Exception as e:
            print(e)
