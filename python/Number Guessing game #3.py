import random
num = random.randint(1,100)
guess = int(input("Guess the number: "))
count = 1

def program():
    while guess != num:
        if guess > num:
            print("too big")
            return
        elif guess < num:
            print("too small")
            return
        count + 1
    if guess == num:
        print("good guess, you took ", count, " attempts to solve it.")
program()
