# prices

PpSqM = 3.75
B = 6.5
S = 18.75
L = 29.5

# what carpet range do customer want?

carpArea = int(input("How many square metres of carpet would you like? - "))
areaPrice = carpArea * PpSqM
    
carpType = input("What range of carpet do you want?:  "
                 "Basic — £6.50 [B]; "
                 "Standard — £18.75 [S]; "
                 "Luxury — £29.50 [L]")

# subprogram and variables for pricing

def bPRICE():
    Bprice = areaPrice + B * carpArea
    print("The total for your choice is: £", Bprice)

def sPRICE():
    Sprice = areaPrice + S * carpArea
    print("The total for your choice is: £", Sprice)

def lPRICE():
    Lprice = areaPrice + L * carpArea
    print("The total for your choice is: £", Lprice)


if carpType == "b" or "B":
    bPRICE()

elif carpType == "s" or "S":
    sPRICE()

elif carpType == "l" or "L":
    lPRICE()
