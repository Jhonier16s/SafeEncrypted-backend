
from cryptography.fernet import Fernet
import base64


def generate_key():
    
    key = Fernet.generate_key()
    return key


def encrypt_file(file_data, key):
    
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode(
        "utf-8"
    )  
    return encrypted_data_base64


def encrypt(files):
    
    print("Encrypting files...")
    key = generate_key()

    encrypted_files = {}

    for file_name, file_data in files.items():
        encrypted_data = encrypt_file(file_data, key)
        encrypted_files[file_name] = encrypted_data

    return key.decode("utf-8"), encrypted_files
