def decryptor(file_name, key):
    #Imports
    import cryptography
    from cryptography.fernet import Fernet

    #Enter the name of file that you want to decrypt
    input_file = file_name
    try:
        #Name of the file that is decrypted
        output_file = "decrypted.csv"

        #Key.
        unlock_key = key
        if len(unlock_key)!= 44:
            raise cryptography.fernet.binascii.Error
        else:
            #Reading the input file for decryption
            with open(input_file, 'rb') as f:
                data = f.read()
            fernet = Fernet(unlock_key)
            decrypted = fernet.decrypt(data)

            #Writing the decrypted file to the output
            with open(output_file, 'wb') as f:
                f.write(decrypted)
            print("The file {} is decrypted successfully and saved as {}".format(input_file,output_file))
    
    #Exceptions
    except cryptography.fernet.InvalidToken:
        print("The key entered is not valid. Please enter the key used at the time of encryption.")
    except cryptography.fernet.binascii.Error:
        print("Your key should be having 44 characters")
    except FileNotFoundError:
        print("The {} file does not exist. Please enter a valid file name with extension for decryption.".format(file_name))
