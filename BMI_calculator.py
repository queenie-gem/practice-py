# creating a BMI calculator using python

def calculate_bmi():
    name = input("Enter your name: ")

    weight = float(input(f" {name}, enter your weight in kg: "))
    height = float(input(f" {name}, enter your height in meters: "))

    BMI = weight / (height * height)

    print(f"Your BMI IS {BMI}")

    if BMI > 0:
        if BMI <= 18.5:
            print(f"{name} you are underweight")
        elif BMI <= 24.9:
            print(f"{name} you are Normal Weight")  
        elif BMI < 29.9:
            print(f"{name} you are Over weight")
        elif BMI <= 34.9:
            print(f"{name} you are Obese")   
        elif BMI <= 39.9:
            print(f"{name} you are severly obese")               
        else:
            print(f"{name} you are morbidly obese")    
    else:
        print("Invalid input, please enter a valid weight and height")

BMI_calculate = True
while BMI_calculate:
    calculate_bmi()
    choice = input("Do you want to calculate your BMI again: yes/no: ")

    if (choice != "yes"):
         BMI_calculate = False
         print("Thanks for using the BMI calculator")


