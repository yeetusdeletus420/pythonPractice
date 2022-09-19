F = 1.20
P = 1.23
G = 1.19
S = 1.21
I = 1.22

p = float(input("What is the price of the shoes?  £"))
c = input("And what country are you buying in? ~ France [F], Portugal [P],"
                                                "Germany [G], Spain [S], Italy [I]")
if c == "f" or "F":
    print("Your total is: £",p*F)
elif c == "p" or "P":
    print("Your total is: £",p*P)
elif c == "g" or "G":
    print("Your total is: £",p*G)
elif c == "s" or "S":
    print("Your total is: £",p*S)
elif c == "i" or "I":
    print("Your total is: £",p*I)
