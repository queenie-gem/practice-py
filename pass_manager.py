"""
Creating Our password manager called Sharry10XY

what it does is simple 

take a username and a password an duses it to encrpt our password and username also without wwebsite data to prevent feature breaches 
"""

import os
import json

# Application configuration

APP_NAME="Sharry10XY"
USERS_FILE="users.json"
WEBSITE_LOGS_FILE="websites_logs.json"

print("======================================================================================")
print(f"Welcome to {APP_NAME}\nYour passwords are in good hands built by the sharry team")
print(f"\n")

# this input checks if the user is a returning user or a new user and if the input is not r or n it will print an error message and quit the application
is_returning_user = input(f"Are you a returning user or a new user (r,n):  ")

if is_returning_user not in ["r", "n"]:
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
# this function checks if a file exist if not it create it and write the data to the file for the applicication to use
def check_and_write_file(filename, data):
    if not os.path.isfile(filename):
        print("Databases doesn't exits creating now")
        with open(filename, "w") as f:
            f.write("[]")
    with open(filename, "w") as f:
        f.write(data)

# this loads the users.json and websites_logs.json files into the users_db and website_logs variables respectively
users_db = check_and_load_file(USERS_FILE)
website_logs = check_and_load_file(WEBSITE_LOGS_FILE)
# this variable will hold the logged in user information after successful login or account creation
logged_in_user = None

# login logic for returning users and new user creation logic for new users
if is_returning_user.lower() == "r":
    print("its nice to have you back")
    username = input("Enter username: ")
    password = input("Enter Password: ")

    if not username or not password:
        print("Username and password is required")
        quit()

    # this conditon loops through the users_db and checks if the username and password match any user in the users_db if it does it sets the logged_in_user to that user and breaks the loop

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

    # this creates a new user and adds it to the users_db and also writes the users_db to the users.json file
    if not username or not password:
        print("Username and password is required")
        quit()

    user = {
        "username": username,
        "password": password,
        "id": len(users_db) + 1
    }
    users_db.append(user)

     # this function checks if the file exists and writes the user_db to the users.json file
    check_and_write_file(USERS_FILE,json.dumps(users_db, indent=4))
    logged_in_user = user
    print("Account created successfully")


def view_all_website_logs():
    print("\nYour saved website accounts:")
    # user_logs = [log for log in website_logs if log["user_id"] == logged_in_user["id"]]

    user_logs = []
    for log in website_logs:
        if log["user_id"] == logged_in_user["id"]:
            user_logs.append(log)

    if not user_logs:
        print("No saved website accounts found.")
        return
    for log in user_logs:
        print(f"Website: {log['website']}, Username: {log['username']}, Password: {log['password']}")    
   

# This function adds a website log to the website_logs.json file with the website, username and password and also adds the user_id to the website log so that we can know which user added the website log 
    
def add_website_log(website, website_username, website_password): 
    log = { "id": len(website_logs) + 1, 
           "website": website, 
           "username": website_username, 
           "password": website_password, 
# This adds the user_id to the website log so that we can know which user added the website log
           "user_id": logged_in_user["id"] 
           }    
    website_logs.append(log) 
    check_and_write_file( WEBSITE_LOGS_FILE, json.dumps(website_logs, indent=4) ) 
    print(f"Website log for {website} added successfully.")

#  this function checks if the user wants to save a website account and if yes it takes the website, username and password and saves it to the website_logs.json file

print("\nDo you want to save a website account?") 

save_website = input("yes/no: ").lower() 
if save_website == "yes": 
    website = input("Enter website: ") 
    website_username = input("Enter website username/email: ") 
    website_password = input("Enter website password: ") 
    if not website or not website_username or not website_password:
        print("Website, username and password is required")
        quit()
    add_website_log( website, website_username, website_password )
else: 
    get_one_website_log = input("Do you want to view a specific website log? (yes/no): ").lower()
    if get_one_website_log == "yes":
        specfic_website_to_retrive = input("Enter website name: ")
        user_logs = []
        for log in website_logs:
            if log["user_id"] == logged_in_user["id"] and log["website"] == specfic_website_to_retrive:
                user_logs.append(log)

        if len(user_logs) == 0:
            print(f"No website found for {specfic_website_to_retrive}")
        for log in user_logs:
            print(f"Website: {log['website']}, Username: {log['username']}, Password: {log['password']}")   

        pass
    else:
        view_all_website_logs()