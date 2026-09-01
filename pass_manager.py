"""
Creating Our password manager called Sharry10XY

what it does is simple 

take a username and a password an duses it to encrpt our password and username also without wwebsite data to prevent feature breaches 
"""

import os
import json

APP_NAME="Sharry10XY"
USERS_FILE="users.json"
WEBSITE_LOGS_FILE="websites_logs.json"

print("======================================================================================")
print(f"Welcome to {APP_NAME}\nYour passwords are in good hands built by the sharry team")
print(f"\n")

is_returnign_user = input(f"Are you a returnign user or a new user (r,n):  ")

if is_returnign_user not in ["r", "n"]:
    print("That seems like an error start the app again")
    quit()

# this function checks if a file exist if not it create it and load the file for the applicication to use
def check_and_load_file(filename):
    if not os.path.isfile(filename):
        print("Databases doesn't exits creating now")
        with open(filename, "w") as f:
            f.write("[]")
    with open(filename, "r") as f:
        return json.load(f)

def check_and_write_file(filename, data):
    if not os.path.isfile(filename):
        print("Databases doesn't exits creating now")
        with open(filename, "w") as f:
            f.write("[]")
    with open(filename, "w") as f:
        f.write(data)

users_db = check_and_load_file(USERS_FILE)
logged_in_user = None

# login logic for returning users 
if is_returnign_user.lower() == "r":
    print("its nice to have you back")
    username = input("Enter username: ")
    password = input("Enter Password: ")

    if not username or not password:
        print("Username and password is required")
        quit()

    # this conditon loops through the user_db and checck if the username equals to the username in the user_db and the checks if the password is correct

    for user in users_db:
        if (user["username"] != username):
            continue

        if (user["password"] == password):
            logged_in_user = user
            break

    if logged_in_user:
        print("Logged In successfully")
            
else: 
    print("It would be wonderful to trust us with your password")
    username = input("Enter username: ")
    password = input("Enter Password: ")
    # this creates a user and adds an id based on the id loop in the user_db
    if not username or not password:
        print("Username and password is required")
        quit()

    user = {
        "username": username,
        "password": password,
        "id": len(users_db) + 1
    }
    users_db.append(user)

     # this function adds new_user and add it back to the user_db
    check_and_write_file(USERS_FILE,json.dumps(users_db, indent=4))
    logged_in_user = user
    print("Account created successfully")
