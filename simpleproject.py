name = input("enter your name: ")
print(f"welcome {name} ")
for i in range(1,6):
    subject = input("enter your subject: ")
    marks = int(input(f"enter your marks in subject {i}: "))
    if marks >= 90:
        print(f"your grade in subject {i} is A+")
    elif marks >= 80:
        print(f"your grade in subject {i} is A")
    elif marks >= 70:
        print(f"your grade in subject {i} is B+")
    elif marks >= 60:
        print(f"your grade in subject {i} is B")
    elif marks >= 50:
        print(f"your grade in subject {i} is C")
    else:
        print(f"your grade in subject {i} is F")