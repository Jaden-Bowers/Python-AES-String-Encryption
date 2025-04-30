import AES256_Basic_Functions

IV = 1234567890123456 #IV in int form
IV = IV.to_bytes(16, 'big') #IV in byte form

#   ---AES with set IV returning encrypted message in hex form---
encrypted_message = AES256_Basic_Functions.AES_encrypt_hex("This is plain text", "Secure password", IV)
print(encrypted_message, "\t\t\t\t- Set IV encrypted message in hex form")

#   ---AES with random IV returning encrypted message in hex form---
encrypted_message, Random_IV  = AES256_Basic_Functions.AES_encrypt_hex("This is plain text", "Secure password")
print(encrypted_message, "\t\t\t\t- Random IV encrypted message in hex form")
print(Random_IV, "\t\t- Random IV")

#   ---Decrypting with encrypted message in hex form--
print(AES256_Basic_Functions.AES_decrypt_hex(encrypted_message, "Secure password", Random_IV), "\t\t\t\t\t\t- Decrypted text\n")



#   ---AES with set IV returning encrypted message in base64 form---
encrypted_message = AES256_Basic_Functions.AES_encrypt_base64("This is plain text", "Secure password", IV)
print(encrypted_message, "\t\t\t\t\t- Set IV encrypted message in base64 form")

#   ---AES with random IV returning encrypted message in base64 form---
encrypted_message, Random_IV  = AES256_Basic_Functions.AES_encrypt_base64("This is plain text", "Secure password")
print(encrypted_message, "\t\t\t\t\t- Random IV encrypted message in base64 form")
print(Random_IV, "\t\t- Random IV")

#   ---Decrypting with encrypted message in base64 form--
print(AES256_Basic_Functions.AES_decrypt_base64(encrypted_message, "Secure password", Random_IV),"\t\t\t\t\t\t- Decrypted text\n")



#   ---AES with set IV returning encrypted message in byte form---
encrypted_message = AES256_Basic_Functions.AES_encrypt_raw("This is plain text", "Secure password", IV)
print(encrypted_message,"\t\t- Set IV encrypted message in byte form")

#   ---AES with random IV returning encrypted message in byte form---
encrypted_message, Random_IV  = AES256_Basic_Functions.AES_encrypt_raw("This is plain text", "Secure password")
print(encrypted_message, "\t\t- Random IV encrypted message in byte form")
print(Random_IV, "\t\t- Random IV")

#   ---Decrypting with encrypted message in byte form--
print(AES256_Basic_Functions.AES_decrypt_raw(encrypted_message, "Secure password", Random_IV), "\t\t\t\t\t\t- Decrypted text\n")