name = input("enter your name: ")
print(f"welcome {name} ")

password_dic = []
def passwordadd(website, username, password):
    new_password = {
        "website": website,
        "username": username,
        "password": password
    }
    password_dic.append(new_password)
website = input("enter your website name: ")
username = input("enter your username: ")
password = input("enter your password: ")

passwordadd(website, username, password)


def viewpassword():
    for password in password_dic:
        print(f"Website: {password['website']}")
        print(f"Username: {password['username']}")
        print(f"Password: {password['password']}")


while True:
    print("1. Add password")
    print("2. View passwords")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        passwordadd(website, username, password)
    elif choice == "2":
        viewpassword()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")        
        
