File Encryptor

        This project can be used for encrypting and decrypting files on Python Language. The encryption is based on the Cryptography module which is compatible for Python Versions 2.7, 3.4 and above. 
  
You can install the module by using the command:
        python -m pip install cryptography

This encryption is based on AES(Advanced Encryption Standard). This is Symmetric Encryption.
Symmetric encryption is when a key is used to encrypt and decrypt a message, so whoever encrypted it can decrypt it. The only way to decrypt the message is to know what was used to encrypt it; kind of like a password.


Usage:
      1. You can use the encryptin.py for encrypting the file.
      2. Once the file is encrypted, you can see the "key.key" file which contains the key. You have to secure          it for decrypting the file in future.
      3. You can decrypt the file using decrytion.py provided "key.key" file (initially used for encryption) is          present on the directory. 
  
