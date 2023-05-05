#!/usr/bin/env python3
'''
Password Manager
Author: CireWire, Helix Corporation
Copywrite: 2023, CireWire, Helix Corporation
License: MIT
Version: 1.0.0
Maintainer: CireWire
Status: Production
Summary: A simple password manager app that allows you to store and retrieve passwords for different services.

'''


# Import modules
from cryptography.fernet import Fernet
import argparse
import pyperclip
import json
import logging

# Generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Load the encryption key from a file
def load_key():
    return open('key.key', 'rb').read()

# Encrypt the password using the encryption key
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt the password using the encryption key
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    return decrypted_password.decode()

# Generate and save a new encryption key
generate_key()

# Load the encryption key
key = load_key()

# Example usage
password = "mysecretpassword123"
encrypted_password = encrypt_password(password, key)
print("Encrypted password:", encrypted_password)

decrypted_password = decrypt_password(encrypted_password, key)
print("Decrypted password:", decrypted_password)



# Function to load passwords from a file
def load_passwords():
    try:
        with open('passwords.json', 'r') as password_file:
            passwords = json.load(password_file)
    except FileNotFoundError:
        passwords = {}
    return passwords

# Function to save passwords to a file
def save_passwords(passwords):
    with open('passwords.json', 'w') as password_file:
        json.dump(passwords, password_file)

# Function to add a new password to the password manager app
def add_password(username, password, service):
    # Load the encryption key
    key = load_key()

    # Load the existing passwords from a file
    passwords = load_passwords()

    # Encrypt the password using the encryption key
    encrypted_password = encrypt_password(password, key)

    # Add the new password to the passwords dictionary
    if service in passwords:
        passwords[service][username] = encrypted_password.decode()
    else:
        passwords[service] = {username: encrypted_password.decode()}

    # Save the updated passwords to a file
    save_passwords(passwords)

    print(f"Added password for {service} - {username}")

# Example usage
add_password("john.doe@example.com", "mysecretpassword123", "Gmail")

# Function to load passwords from a file
def load_passwords():
    try:
        with open('passwords.json', 'r') as password_file:
            passwords = json.load(password_file)
    except FileNotFoundError:
        passwords = {}
    return passwords

# Function to save passwords to a file
def save_passwords(passwords):
    with open('passwords.json', 'w') as password_file:
        json.dump(passwords, password_file)

# Function to retrieve a password from the password manager app
def get_password(username, service):
    # Load the encryption key
    key = load_key()

    # Load the existing passwords from a file
    passwords = load_passwords()

    # Check if the service exists in the passwords dictionary
    if service not in passwords:
        print(f"No passwords found for {service}")
        return

    # Check if the username exists for the service in the passwords dictionary
    if username not in passwords[service]:
        print(f"No password found for {username} - {service}")
        return

    # Decrypt the password using the encryption key
    encrypted_password = passwords[service][username].encode()
    decrypted_password = decrypt_password(encrypted_password, key)

    # Copy the password to the clipboard for easy pasting
    pyperclip.copy(decrypted_password.decode())

    print(f"Copied password for {username} - {service} to clipboard")

# Example usage
get_password("john.doe@example.com", "Gmail")

# Function to save a new password to the password manager app
def save_password(username, password, service):
    # Load the encryption key
    key = load_key()

    # Load the existing passwords from a file
    passwords = load_passwords()

    # Encrypt the password using the encryption key
    encrypted_password = encrypt_password(password.encode(), key)

    # Add the password to the passwords dictionary
    if service in passwords:
        passwords[service][username] = encrypted_password.decode()
    else:
        passwords[service] = {username: encrypted_password.decode()}

    # Save the updated passwords to a file
    save_passwords(passwords)

    print(f"Saved password for {username} - {service}")

# Function to retrieve a password from the password manager app
def get_password(username, service):
    # Load the encryption key
    key = load_key()

    # Load the existing passwords from a file
    passwords = load_passwords()

    # Check if the service exists in the passwords dictionary
    if service in passwords and username in passwords[service]:
        # Retrieve the encrypted password from the passwords dictionary
        encrypted_password = passwords[service][username]

        # Decrypt the password using the encryption key
        decrypted_password = decrypt_password(encrypted_password.encode(), key)

        # Copy the password to the clipboard
        pyperclip.copy(decrypted_password.decode())

        print(f"Password for {username} - {service} copied to clipboard")
    else:
        print(f"No password found for {username} - {service}")

# Set up the logging configuration
logging.basicConfig(filename='password_manager.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Function to retrieve a password from the password manager app
def get_password(username, service):
    # Load the encryption key
    key = load_key()

    # Load the existing passwords from a file
    passwords = load_passwords()

    # Check if the service exists in the passwords dictionary
    if service in passwords and username in passwords[service]:
        # Retrieve the encrypted password from the passwords dictionary
        encrypted_password = passwords[service][username]

        # Decrypt the password using the encryption key
        decrypted_password = decrypt_password(encrypted_password.encode(), key)

        # Copy the password to the clipboard
        pyperclip.copy(decrypted_password.decode())

        logging.info(f"Password for {username} - {service} copied to clipboard")
        print(f"Password for {username} - {service} copied to clipboard")
    else:
        logging.warning(f"No password found for {username} - {service}")
        print(f"No password found for {username} - {service}")
