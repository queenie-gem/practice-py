passwords = []

def add_password(website, username, password):
    new_password = {
        "website": website,
        "username": username,
        "password": password
    }
    passwords.append(new_password)
    
website = input("Enter website: ")
username = input("Enter username: ")
password = input("Enter password: ")

add_password(website, username, password)
print(passwords)