def calc():
    num1 = int(input("What numbers do you want to add together? ~ First one here: "))
    num2 = int(input("Now what is your second number?: "))
    print(num1+num2)

def ask():
    access = input("Hi there! Do you want to access calculator? ~ Y or N")
    if access == "y" or "Y":
        calc()
    elif access == "n" or "N":
        choice = input("Then would you like to quit? ~ Y or N")
        if choice == "y" or "Y":
            quit
        elif choice == "n" or "N":
            print("okay boomer, you transaction was denied :)")
ask()
