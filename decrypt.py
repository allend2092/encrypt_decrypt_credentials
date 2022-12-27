# decrypt credentials. make sure you have the key and iv.

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
key = b'< IMPORT KEY FROM encrypt.py script>'
iv = b'< IMPORT iv FROM encrypt.py script>'

# Read the encrypted credentials from the file
with open('credentials.txt', 'r') as f:
  encrypted_credentials = f.read()

# Decrypt the credentials
decrypted_credentials = decrypt(encrypted_credentials)

# Split the decrypted credentials into username and password
username, password = decrypted_credentials.split(':')
