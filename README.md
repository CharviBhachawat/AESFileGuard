# AESFileGuard
SecureFileCrypt is a Python-based command-line tool designed to enhance the security of your sensitive files through robust encryption and decryption processes. With this tool, you can protect your confidential data by applying Advanced Encryption Standard (AES) algorithms, ensuring a high level of security for your files.

Key Features:

1. Strong Encryption: Utilizes the AES encryption algorithm, a widely accepted and secure standard for protecting data confidentiality.

2. User-Friendly Interface: The tool provides a simple and intuitive command-line interface, allowing users to easily encrypt and decrypt files with minimal effort.

3. Password Protection: Enhances security by prompting users to input a password during both encryption and decryption processes. The tool utilizes a key derivation function to derive encryption keys from user passwords.

4. Randomness and Salting: Incorporates randomness through secure random number generation for salting. This ensures unique encryption keys, even for the same password.

5. File Handling: Efficiently reads content from the original file, encrypts it, and writes the encrypted content to a new file. During decryption, the process is reversed, allowing for seamless file recovery.

How to use

### Python Dependencies

1. **Install Python:**
   - Make sure you have Python installed on your system. If not, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Cryptography Library:**
   - Open a terminal or command prompt.
   - Run the following command to install the required Python cryptography library:
   
     pip install cryptography
    
## How to Use

# Step 1: Open a terminal or command prompt on your computer.

# Step 2: Navigate to the directory containing the 'code.py' script.
# Use the 'cd' command to change the directory. For example:
cd path/to/directory

# Step 3: Run the following command to encrypt a file:
python code.py encrypt -f path/to/original/file.txt
# Replace 'path/to/original/file.txt' with the actual path to the file you want to encrypt.

# Step 4: Follow the on-screen prompts to enter a strong password when prompted.

# Step 5: The tool will generate a secure encrypted file with a ".encrypted" extension.

# To decrypt the file, run the following command:
python code.py decrypt -f path/to/encrypted/file.txt.encrypted
# Replace 'path/to/encrypted/file.txt.encrypted' with the path to the encrypted file.

# Step 6: Enter the correct password used during encryption when prompted.

# Step 7: The tool will recover your original file and save it in the same directory.
