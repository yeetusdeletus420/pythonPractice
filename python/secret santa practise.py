list = ["Jerry", "Zoe", "Felix", "Quin"]

import random
randnum = random.randint(0,len(list))

def partnerView():
    askName = str(input("What's your name? "))
    genName = str(input("Do you want to know who your Secret Santa partner is? "))
    if input == "y" or "Y":
        print(askName, ", your Secret Santa partner is ", list[randnum], ".")
        del list[randnum]
    elif input == "n" or "N":
        print("Alright then.")
        exit
partnerView()

if list == 0:
    print("That's everyone! Thanks for using.")
    exit

addName = str(input("Do you want to add your name to the list?"))
if addName == "y" or "Y":
    list.append(askName)
elif addName == "n" or "N":
    exit
