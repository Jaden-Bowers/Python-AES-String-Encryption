# Python AES256 String Encryption
Basic python functions using the pycryptodome library
#

### Must install pycryptodome library ###

```
pip install pycryptodome
```
#
AES256_Basic_Functions.py includes basic functions for encrypting strings using AES256 functions are listed below

Functions     | Description
------------- | -------------
AES_encrypt_hex  | Accepts plain text message, Password, and IV (if not specified then will return random IV)<br />Returns hex value of encrypted_message and if not specified the bytes value of the random iv
AES_decrypt_hex  | Accepts encrypted message in hex form, Password, IV<br />Returns plain text value of your hex message and password
AES_encrypt_base64 | Accepts plain text message, Password, and IV (if not specified then will return random IV)<br />Returns base64 value of encrypted_message and if not specified the bytes value of the random iv
AES_decrypt_base64 | Accepts encrypted message in base64 form, Password, IV<br />Returns plain text value of your hex message and password
AES_encrypt_raw | Accepts plain text message, Password, and IV (if not specified then will return random IV)<br />Returns byte value of encrypted_message and if not specified the bytes value of the random iv
AES_decrypt_raw | Accepts encrypted message in byte form, Password, IV<br />Returns plain text value of your hex message and password

#

AES256-Basic-Examples.py shows the basic use cases of the functions

When ran the output should look similar to below
```
32243464b6a2d8a9f8e1f041ddaf28ba56c4                              - Set IV encrypted message in hex form
cb05230d14944766c0dea7d773487b30d98b                              - Random IV encrypted message in hex form
b'H\xd51B\t\xd1\x95\x08GgsMS~\xf3g'                               - Random IV
This is plain text                                                - Decrypted text

MiQ0ZLai2Kn44fBB3a8oulbE                                          - Set IV encrypted message in base64 form
WkpHKAs2CpAlqsz3GHdUcGr7                                          - Random IV encrypted message in base64 form
b'>\x14\x7f\x9d;\x03\xab\xfca|\x12Lg\xb4Y\xee'                    - Random IV
This is plain text                                                - Decrypted text

b'2$4d\xb6\xa2\xd8\xa9\xf8\xe1\xf0A\xdd\xaf(\xbaV\xc4'            - Set IV encrypted message in byte form
b'\xa3\x06\x9b\x93\x81\\\xddM\x15"\xd0\x8c\xb6\x83\xce\xe8p\x14'  - Random IV encrypted message in byte form
b'h\x06\x02C\xec\xc3\xe0b\x81\xa8"\n\x02\x9c\x90,'                - Random IV
This is plain text                                                - Decrypted text
```
