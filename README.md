File Encryptor

        This project can be used for encrypting and decrypting csv files on Python Language. The encryption is based on the Cryptography module which is compatible for Python Versions 2.7, 3.4 and above. 
  
You can install the module by using the command:

        python -m pip install cryptography

This encryption is based on AES(Advanced Encryption Standard). This is Symmetric Encryption.
Symmetric encryption is when a key is used to encrypt and decrypt a message, so whoever encrypted it can decrypt it. The only way to decrypt the message is to know what was used to encrypt it; kind of like a password.


**USAGE**

**Copy the encryption.py and decryption.py files to the desired directory.**

***For Encryption***

1. *Import the 'encryptor' function from Encryption.py file using the following command:*
        
        **from encryption import encryptor**

2. *Call the encryptor function and also give filename with extension as argument.*
        
        **encryptor("example.csv")**

3. *If the filename provided is valid, the provided file will be encrypted named as **'out.encrypted'** and a file named "key.key" will be created on your directory. This file contains the value of key, save this for future decryption of encrypted file.*

***For Decryption***

1. *Import the 'decryptor' function from Decryption.py file using the following command:*
        
        **from decryption import decryptor**

2. *Call the decryptor function with **encrypted file and key(variable which contains value of key at the time of encryption)** as arguments.*
        
        **decryptor(encrypted_file, key)**

3. *If filename and provided key are valid, the file will decrypted and will be saved as **"decrypted.csv"**.*

***THANKS!!!***
  
