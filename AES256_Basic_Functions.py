import hashlib
from Crypto.Cipher import AES
from base64 import b64decode, b64encode

def AES_encrypt_hex (message, password, IV="Place Holder Initialization Vector"):
    '''
    message: Your plain text message that you would like to encrypt
    password: Your password that will be used as a key to the encryption
    IV: Initialization Vector (must be 16 btyes) and in byte format. Leave blank for random
    return: returns hex value of encrypted_message and if not specified the bytes value of the random iv
    '''

    tkey = hashlib.sha256(password.encode()).hexdigest() #Converts password into sha256 hash
    key = tkey[:64 - 32].encode() #Removes the last 32 characters of the hash (this is done becasuse AES only takes keys with a length of 16 , 24 or 32 bytes)

    if IV == "Place Holder Initialization Vector": #If user does not specify IV then generate 16 random byte to be used for IV
        cipher = AES.new(key, AES.MODE_CFB) # cipher object with random IV
        encrypted_message = cipher.encrypt(message.encode()) #encrypted message in byte form
        return encrypted_message.hex(), cipher.iv #Covert encrypted message from byte to hex and get the random IV from the cipher object
    else:
        cipher = AES.new(key, AES.MODE_CFB, iv=IV) # cipher object with set IV
        encrypted_message = cipher.encrypt(message.encode()) #encrypted message in byte form
        return encrypted_message.hex() #Covert encrypted message from byte to hex

def AES_decrypt_hex (encrypted_message, password, IV):
    '''
    encrypted_message: Your encrypted message that you would like to decrypt
    password: Your password that will be used as a key to the decryption
    IV: Initialization Vector of the cipher when encrypted in byte form
    return: returns plain text value of your hex message and password
    '''

    tkey = hashlib.sha256(password.encode()).hexdigest() #Converts password into sha256 hash
    key = tkey[:64 - 32].encode() #Removes the last 32 characters of the hash (this is done becasuse AES only takes keys with a length of 16 , 24 or 32 bytes)

    encrypted_message = bytes.fromhex(str(encrypted_message)) #encrypted message in byte form
    
    cipher = AES.new(key, AES.MODE_CFB, iv=IV) #cipher object

    return cipher.decrypt(encrypted_message).decode() #Decrypt encrypted message in byte form

def AES_encrypt_base64(message, password, IV="Place Holder Initialization Vector"):
    '''
    message: Your plain text message that you would like to encrypt
    password: Your password that will be used as a key to the encryption
    IV: Initialization Vector of the cipher when encrypted in byte form
    return: returns base64 value of encrypted_message and iv
    '''

    tkey = hashlib.sha256(password.encode()).hexdigest() #Converts password into sha256 hash
    key = tkey[:64 - 32].encode() #Removes the last 32 characters of the hash (this is done becasuse AES only takes keys with a length of 16 , 24 or 32 bytes)
    
    if IV == "Place Holder Initialization Vector": #If user does not specify IV then generate 16 random byte to be used for IV
        cipher = AES.new(key, AES.MODE_CFB) # cipher object with random IV
        cipher_bytes = cipher.encrypt(message.encode()) #encrypted message in byte form
        encrypted_message = b64encode(cipher_bytes) # Format bytes to base64
        return encrypted_message.decode(), cipher.iv #Covert encrypted message from byte to hex and get the random IV from the cipher object
    else:
        cipher = AES.new(key, AES.MODE_CFB, iv=IV) # cipher object with set IV
        cipher_bytes = cipher.encrypt(message.encode()) #encrypted message in byte form
        encrypted_message = b64encode(cipher_bytes) # Format bytes to base64
        return encrypted_message.decode()
    

def AES_decrypt_base64(encrypted_message, password, IV):
    '''
    encrypted_message: Your encrypted message that you would like to decrypt in base64
    password: Your password that will be used as a key to the decryption
    IV: Initialization Vector of the cipher when encrypted in base64 form
    return: returns plain text value of your base64 message and password
    '''

    tkey = hashlib.sha256(password.encode()).hexdigest() #Converts password into sha256 hash
    key = tkey[:64 - 32].encode() #Removes the last 32 characters of the hash (this is done becasuse AES only takes keys with a length of 16 , 24 or 32 bytes)

    encrypted_message = b64decode(encrypted_message) # Converts base64 message to bytes
    
    cipher = AES.new(key, AES.MODE_CFB, iv=IV) #cipher object

    return cipher.decrypt(encrypted_message).decode()

def AES_encrypt_raw (message, password, IV="Place Holder Initialization Vector"):
    '''
    message: Your plain text message that you would like to encrypt
    password: Your password that will be used as a key to the encryption
    return: returns bytes value of encrypted_message and iv
    '''
    tkey = hashlib.sha256(password.encode()).hexdigest() #Converts password into sha256 hash
    key = tkey[:64 - 32].encode() #Removes the last 32 characters of the hash (this is done becasuse AES only takes keys with a length of 16 , 24 or 32 bytes)
    
    if IV == "Place Holder Initialization Vector": #If user does not specify IV then generate 16 random byte to be used for IV
        cipher = AES.new(key, AES.MODE_CFB) # cipher object with random IV
        encrypted_message = cipher.encrypt(message.encode()) #encrypted message in byte form
        return encrypted_message, cipher.iv
    else:
        cipher = AES.new(key, AES.MODE_CFB, iv=IV) # cipher object with set IV
        encrypted_message = cipher.encrypt(message.encode()) #encrypted message in byte form
        return encrypted_message

def AES_decrypt_raw(encrypted_message, password, IV):
    '''
    encrypted_message: Your encrypted message that you would like to decrypt in byte form
    password: Your password that will be used as a key to the decryption
    IV: Initialization Vector of the cipher when encrypted in bytes form
    return: returns plain text value of your bytes message and password
    '''

    tkey = hashlib.sha256(password.encode()).hexdigest() #Converts password into sha256 hash
    key = tkey[:64 - 32].encode() #Removes the last 32 characters of the hash (this is done becasuse AES only takes keys with a length of 16 , 24 or 32 bytes)
    
    cipher = AES.new(key, AES.MODE_CFB, iv=IV)

    return cipher.decrypt(encrypted_message).decode()