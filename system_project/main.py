import json
import os
import time
import getpass

def read_json():
    with open("profile.json", "r") as read_file:
        data = json.load(read_file)
        return data

if not os.path.exists("profile.json") or os.path.getsize("profile.json") == 0:
    new_username = input("Enter your new username: ")
    new_user_password = getpass.getpass("Enter your new password: ")

    user_data = {
        "user": new_username,
        "password": new_user_password
    }

    with open("profile.json", "w") as file:
        json.dump(user_data, file, indent=4)
else:
    data = read_json()

    while True:
        os.system('clear')
        print("--- LOGIN SYSTEM ---")

        log_username = input("Enter username: ")
        log_user_password = getpass.getpass("Enter pasword: ")

        if log_username == data.get('user') and log_user_password == data.get('password'):
            print(f"\nWelcome {data['user']}\n")
            break  
        else:
            print("\n[!] Invalid username or password.")
            time.sleep(2)
            continue
