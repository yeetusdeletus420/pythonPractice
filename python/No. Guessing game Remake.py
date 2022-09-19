import random
number = random.randint(1,100)
count = 1

attempt = int(input("Guess my number: ")):
    while attempt != number:
        if attempt > number:
            print("too high")
        elif attempt < number:
            print("too low")
        count + 1
        return


if attempt == number:
    print("Congrats, you took ", count, " attempts to beat the game.")
