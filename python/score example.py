def score():
    score = 0

while True:
    yeet=input("click 'y' if you want to add to your score, and 'n' if you want to subtract")
    if yeet == "y".lower():
        score() + 1
        print(score)
    elif yeet == "n".lower():
        score() - 1
        print(score)
