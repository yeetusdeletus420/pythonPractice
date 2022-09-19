name = input("What ur name?")

def askName():
    ask = str(input("Do you want to see your name? ~ Y or N"))
    
    if ask == "y" or "Y":
        print(name)
        
    elif ask == "n" or "N":
        print("ok")

askName()
