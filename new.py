
password = 1234
ID = 100
p = int(input("Input password: "))
Id = int(input("enter ID no.: "))
age = int(input("enter Age: "))

if p == password:
    print("logged in")
             
    if age < 18:
        print("You got 10 % Discount")
        course_fee = int(input("enter course fee amount: "))
        discount = 10 / 100 * course_fee
        DF = course_fee - discount
        print(F"The discounted fee = {DF}")
        if Id==ID:
            print(" plus 2 % DISCOUNT")
            course_fee = DF
            D = 2 / 100 * course_fee
            DF = course_fee - D
            print(F"The discounted fee = {DF}")
        else:
            print(F"The discounted fee = {DF}")  
    elif age >= 18 and age <= 20:
        print("You got 5 % Discount")
        course_fee = int(input("enter course fee amount: "))
        discount = 5 / 100 * course_fee
        DF = course_fee - discount
        print(F"The discounted fee = {DF}")
        if Id == ID:
            print("plus 2 % Discount")
            course_fee = DF
            D = 2 / 100 * course_fee
            DF = course_fee - D
            print(F"The discounted fee = {DF}")
        else:
            print(F"The discounted fee = {DF}") 
    else:
        print("INVALID AGE")       
    
else:
    print("INVALID PASSWORD")           