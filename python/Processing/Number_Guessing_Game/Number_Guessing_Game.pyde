import random
number = random.randint(1,100)
attempt = int(input("What is number?"))
count = 1

while attempt != number:
    if attempt > number:
        print("too high")
    elif attempt < number:
        print("too low")
    count + 1
if attempt == number:
    print("well done, you took ", count, "attempts at this game")
