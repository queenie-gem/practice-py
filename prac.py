#  create a counter
count = 1
attempt = 3
while count <= 3:
    password = "Admin1234"

    p = input("enter password: ")
    if p == password:
        print("Log in successful")   

        choice = int(input("Select choice: \n AOT (Area of Triangle) \n "))

        if choice == 1:
            print("you chose AOT")
            b = int(input("input the value of base: "))
            h = int(input("input the value of height: "))
            AOT = 1/2 * b * h
            print(f"the value of AOT = {AOT}")
            tocontinue = input("Enter 0 to END or 1 to continue: ")  
            if tocontinue == "0":
                print("END")
                exit()
            elif tocontinue == "1":
                print("WELCOME BACK")   
            else:
                print("IDIOT you have been blocked")  
                exit()   
          
        elif choice == 2:
            print("you chose AOR")
            l = int(input("input the vlue of lenght: "))
            b = int(input("inpit the value of breath: "))
            AOR = l * b
            print(f"the value oof AOR = {AOR}")
            tocontinue = input("Enter 0 to END or 1 to continue: ")  
            if tocontinue == "0":
                print("END")
                exit()
            elif tocontinue == "1":
                print("WELCOME BACK")   
            else:
                print("IDIOT you have been blocked")  
                exit()       
            
        elif choice == 3:
            print("you chose AOC") 
            pi = float(input("input the value of pi: "))
            r = int(input("input the value of radius: "))
            AOC = pi * r * r
            print(f"the value of AOC = {AOC}")
            tocontinue = input("Enter 0 to END or 1 to continue: ")  
            if tocontinue == "0":
                print("END")
                exit()
            elif tocontinue == "1":
                print("WELCOME BACK")   
            else:
                print("IDIOT you have been blocked")  
                exit()       
                
           
        elif choice == 4:
            print("you chose AOS") 
            l = int(input("input the value of lenght: "))
            AOS = l * l
            print(f"the vlue of AOS = {AOS}")
            tocontinue = input("Enter 0 to END or 1 to continue: ")  
            if tocontinue == "0":
                print("END")
                exit()
            elif tocontinue == "1":
                print("WELCOME BACK")   
            else:
                print("IDIOT you have been blocked")  
                exit()       
            
        elif choice == 5:
            print("you chose SI")
            p = int(input("input the value of principal: "))
            r = int(input("input the value of rate: "))
            t = int(input("input the value of time: "))       
            SI = p * r * t / 100
            print(f"the value of SI = {SI}")
            tocontinue = input("Enter 0 to END or 1 to continue: ")  
            if tocontinue == "0":
                print("END")
                exit()
            elif tocontinue == "1":
                print("WELCOME BACK")   
            else:
                print("IDIOT you have been blocked")  
                exit()       
            
        else:
            print("INVALID INPUT") 
            tocontinue = input("Enter 0 to END or 1 to continue: ")  
            if tocontinue == "0":
                print("END")
                exit()
            elif tocontinue == "1":
                print("WELCOME BACK")   
            else:
                print("IDIOT you have been blocked")  
                exit()   
            
    else:
        print("Incorrect password ")   
        attempt -= 1
        count += 1
        if attempt > 1:
            print(f"You have {attempt} attempts left")
        elif attempt == 1:
            print(f" You have only {attempt} attempt left")
        else:
            print("IDIOT you dont know your password \n You have been blocked")    
           
