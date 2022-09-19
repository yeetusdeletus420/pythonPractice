import random 
moves = ["rock", "paper", "scissors"]

comScore = 0
uScore = 0

def theirScore():
    comScore+1
def yourScore():
    uScore+1

pcMove = random.choice(moves)

def leaveGame():
    print("""
Your score: """,uScore,"""
Computer score: """,comScore)
    leave = input("So you want to stop playing? ~ [Y]es, [N]o --> ")
    if leave == "y".lower():
        quit
    elif leave == "n".lower():
        game()

# your gameplay

def game():
    while True:
        print("""
This is rock-paper-scissors, and you type in one of the following as a move:
""", moves)

        playerMove = str(input("Rock, paper scissors! --> "))


        if playerMove == pcMove:
            print("""
Your score: """,uScore,"""
Computer score: """,comScore)
            m1 = input("Nothing happens; go again? ~ [Y]es, [N]o --> ")
            if m1 == "y".lower():
                continue
            elif m1 == "n".lower():
                break
                leaveGame()

# your move = rock

        elif (playerMove == moves[0]) and (pcMove == moves[1]):
            theirScore()
            print("""
    Your score: """,uScore,"""
    Computer score: """,comScore)
            m2 = input("Paper over rock! Go again? ~ [Y]es, [N]o --> ")
            if m2 == "y".lower():
                continue
            elif m2 == "n".lower():
                break
                leaveGame()            
        elif (playerMove == moves[0]) and (pcMove == moves[2]):
            yourScore()
            print("""
    Your score: """,uScore,"""
    Computer score: """,comScore)
            m3 = input("Rock smashes scissors! Go again? ~ [Y]es, [N]o --> ")
            if m3 == "y".lower():
                continue
            elif m3 == "n".lower():
                break
                leaveGame()

    # your move = paper

        elif (playerMove == moves[1]) and (pcMove == moves[0]):
            yourScore()
            print("""
    Your score: """,uScore,"""
    Computer score: """,comScore)
            m4 = input("Paper covers rock! Go again? ~ [Y]es, [N]o --> ")
            if m4 == "y".lower():
                continue
            elif m4 == "n".lower():
                break
                leaveGame()
        elif (playerMove == moves[1]) and (pcMove == moves[2]):
            theirScore()
            print("""
    Your score: """,uScore,"""
    Computer score: """,comScore)
            m5 = input("Scissors cut paper! Go again? ~ [Y]es, [N]o --> ")
            if m5 == "y".lower():
                continue
            elif m5 == "n".lower():
                break
                leaveGame()

    # your move = scissors

        elif (playerMove == moves[2]) and (pcMove == moves[0]):
            theirScore()
            print("""
    Your score: """,uScore,"""
    Computer score: """,comScore)
            m6 = input("Rock smashes scissors! Go again? ~ [Y]es, [N]o --> ")
            if m6 == "y".lower():
                continue
            elif m6 == "n".lower():
                break
                leaveGame()
        elif (playerMove == moves[2]) and (pcMove == moves[1]):
            yourScore()
            print("""
    Your score: """,uScore,"""
    Computer score: """,comScore)
            m7 = input("Scissors cut paper! Go again? ~ [Y]es, [N]o --> ")
            if m7 == "y".lower():
                continue
            elif m7 == "n".lower():
                break
                leaveGame()
game()
