from cryptography.fernet import Fernet
import os.path
import base64

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key,'\n')

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def read_master_pwd():
    with open("m-pwd.pwd", "r") as f:
        pwd = f.read()
        return pwd

if not os.path.isfile("m-pwd.pwd"):
    master_password = input("Create your master password: ")
    with open("m-pwd.pwd", "w") as f:
        f.write(str(base64.b64encode(master_password.encode())))
        print("Master password was created.")
else:
    master_password = input("Login with your master password: ")
    if str(base64.b64encode(master_password.encode())) != str(read_master_pwd()):
            print("Wrong password.")
            exit()
    

key = load_key()
fer = Fernet(key)

def add_pwd():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(f'{name}|{fer.encrypt(pwd.encode()).decode()}\n')
        print("Password was added.")

def view_pwd():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print(f"Name: {name}\nPwd: {fer.decrypt(password.encode()).decode()}")

if not os.path.isfile("key.key"):
    write_key()
    print("Key file was created.")

if not os.path.isfile("passwords.txt"):
    with open("passwords.txt", "w") as f:
        print("Passwords file was created.")

while True:
    mode = input("Would you like to add a new password or view an existing one? (add or view), press 'Q' to quit.\n").lower()
    
    if mode == "q":
        break

    elif mode == "add":
        add_pwd()

    elif mode == "view":
        view_pwd()
    
    else:
        print("Incorrect mode!")
        continue