from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path, password):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    with open(file_path, 'rb') as file:
        data = file.read()

    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(salt + iv + encrypted_data)

def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        salt = encrypted_file.read(16)
        iv = encrypted_file.read(16)
        key = generate_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

        encrypted_data = encrypted_file.read()
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

        with open(encrypted_file_path[:-10], 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

def main():
    print("File Encryption and Decryption Tool")

    while True:
        print("\n1. Encrypt File\n2. Decrypt File\n0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            file_path = input("Enter the path of the file to encrypt: ")
            password = input("Enter the encryption password: ")
            encrypt_file(file_path, password)
            print("File encrypted successfully. Encrypted file: {}.encrypted".format(file_path))
        elif choice == 2:
            encrypted_file_path = input("Enter the path of the encrypted file: ")
            password = input("Enter the decryption password: ")
            decrypt_file(encrypted_file_path, password)
            print("File decrypted successfully. Decrypted file: {}".format(encrypted_file_path[:-10]))
        elif choice == 0:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
