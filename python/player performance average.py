import statistics
print("For each of the past 7 games, enter a number from 0 to 10 to rate a player based on performance. You will then get an average player performance score.")

num1 = float(input("Game 1 performance? - "))
num2 = float(input("Game 2 performance? - "))
num3 = float(input("Game 3 performance? - "))
num4 = float(input("Game 4 performance? - "))
num5 = float(input("Game 5 performance? - "))
num6 = float(input("Game 6 performance? - "))
num7 = float(input("Game 7 performance? - "))

scores = num1,num2,num3,num4,num5,num6,num7

print("The average performance score was ", round(statistics.mean(scores), 1))
