import random
b = int(input("How many bits? "))
print(bin(random.randint(0,2**b))[-b:])
