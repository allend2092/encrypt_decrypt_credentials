# This short script will encrypt credentials and save the encrypted credentials to a file.
# You can use this to save credentials that can be accessed by other scripts needing to use credentials to login to
# servers. Import the ecrypted creds, then decrypt and use the creds

# Import the necessary libraries
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import os
import secrets

def generate_key(length):
  # Generate a random bytes object with the specified length
  key = os.urandom(length)

  # Return the key as a bytes object
  return key

def encrypt(plaintext):
  # Pad the plaintext to a multiple of 16 bytes
  plaintext = plaintext + b' ' * (16 - len(plaintext) % 16)

  # Create an AES cipher and encrypt the plaintext
  cipher = AES.new(key, AES.MODE_CBC, iv)
  ciphertext = cipher.encrypt(plaintext)

  # Return the ciphertext as a hexadecimal string
  return ciphertext.hex()

def decrypt(ciphertext):
  # Convert the hexadecimal ciphertext string to bytes
  ciphertext = bytes.fromhex(ciphertext)

  # Create an AES cipher and decrypt the ciphertext
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = cipher.decrypt(ciphertext)

  # Return the plaintext as a string
  return plaintext.decode()


# Set the encryption key and initialization vector
key = generate_key(16)
iv = generate_key(16)

# Print the key and iv for future decryption
print(key)
print(iv)

# Encrypt the credentials
credentials = 'daryl:test-creds123!'
encrypted_credentials = encrypt(credentials.encode())

# Write the encrypted credentials to a file
with open('credentials.txt', 'w') as f:
  f.write(encrypted_credentials)

# Read the encrypted credentials from the file
with open('credentials.txt', 'r') as f:
  encrypted_credentials = f.read()

# Decrypt the credentials
decrypted_credentials = decrypt(encrypted_credentials)

# Split the decrypted credentials into username and password
username, password = decrypted_credentials.split(':')

# Print username and password as a validation step that the script is working. 
print(username)
print(password)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
