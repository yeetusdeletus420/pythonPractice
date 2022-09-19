anime = {}

prompt = str(input("Would you like to add a new entry? "))
if prompt == "y" or "Y":
    entry = str(input("What anime did you like? "))
    anime[entry] = int(input("Rate this anime from 1 to 10: "))
elif prompt == "n" or "N":
    print("very well ...")
