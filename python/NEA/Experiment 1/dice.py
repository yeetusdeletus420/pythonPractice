from random import seed
from random import randint

cycle = 1
p=1
D1 = 0
D2 = 0
while cycle < 6:
    
    s1 = input("P1 enter: ")
    seed = s1
    D1a = randint(1,6)
    D1b = randint(1,6)
    D1 = D1 + D1a + D1b

    p=2
    s2 = input("P2 enter: ")
    seed = s2
    D2a = randint(1,6)
    D2b = randint(1,6)
    D2 = D2 + D2a + D2b
    p=1
    
    cycle = cycle + 1
if D1 > D2:
    print("P1 won!")
if D1 < D2:
    print("P2 won!")
if D1==D2:
    print("draw")
