# Password-manager

This is a simple command-line password manager application written in Python. It allows you to securely store and retrieve passwords for various accounts using encryption.
**Note: This is a test project created for learning purposes and should not be used in a production environment.**

## Features

- Create a master password for accessing the password manager
- Add new passwords for different accounts
- View stored passwords for existing accounts
- Encryption and decryption of passwords using the Fernet cryptography library

## Prerequisites

- Python 3.x
- cryptography library (install using `pip install cryptography`)

## Usage

1. Run the `password-manager.py` script.
2. If it's your first time running the script, you'll be prompted to create a master password. This password will be used to access the password manager in subsequent runs.
3. After entering the master password, you'll be presented with a menu to either add a new password or view existing passwords.
4. To add a new password, select the "add" option, enter the account name, and provide the password.
5. To view existing passwords, select the "view" option. The script will display all stored account names and their corresponding decrypted passwords.
6. To quit the application, enter "q" at the menu prompt.

## File Structure

- `password-manager.py:` The main script containing the password manager functionality.
- `key.key:` A file containing the encryption key used for encrypting and decrypting passwords.
- `m-pwd.pwd:` A file containing the base64-encoded master password.
- `passwords.txt:` A text file where the encrypted account names and passwords are stored.
