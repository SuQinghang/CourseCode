    Cipher = DES_encrypt('plaintext.txt','key1.txt')
    print('密文: ',Cipher)
    plaintext = DES_decrypt('Cipher1.txt','key2.txt')
    print('解密后的明文: ',plaintext)
    Cipher = DES_encrypt('plaintext1.txt','key1.txt')
    print('密文: ',Cipher)