def add():
    Anum1 = float(input("What is the first no. you want to add? ~ "))
    Anum2 = float(input("And the second no.? ~ "))
    print(Anum1+Anum2)

def subtract():
    Snum1 = float(input("What do you want to subtract from? ~ "))
    Snum2 = float(input("And will you subtract by? ~ "))
    print(Snum1-Snum2)

def multiply():
    Mnum1 = float(input("What is your first factor? ~ "))
    Mnum2 = float(input("And your second factor? ~ "))
    print(Mnum1*Mnum2)

def divide():
    Dnum1 = float(input("What will you divide? ~ "))
    Dnum2 = float(input("And what is your divisor? ~ "))
    print(Dnum1/Dnum2)

def square():
    num = float(input("What no. do you want to square? ~ "))
    print(num**num)

def functionCall():
    callFunction = str(input("""
    Function? —

    Addition [A],
    ubtraction [S],
    Multiplication [M],
    Division [D],
    Square [Sq]

    """))

    if callFunction.lower() == "a":
        add()
    elif callFunction.lower() == "s":
        subtract()
    elif callFunction.lower() == "m":
        multiply()
    elif callFunction.lower() == "d":
        divide()
    elif callFunction.lower() == "sq":
        square()
functionCall()

def quitBot():
    ask = input("Are you sure you want to quit? ~ Y or N ")
    if ask.lower() == "y":
        quit()
    elif ask.lower() == "n":
        functionCall()
        
while True:
    askAgain = input("Would you like to call another function? ~ Y or N ")
    if askAgain.lower() == "y":
        functionCall()
    elif askAgain.lower() == "n":
        quitBot()
