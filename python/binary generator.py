import random
string = []
bits = input("How many bits: ")
a = -1
space = [" "]

for i in bits:
    string = string + space
    a=a+1
    string[a] = random()
print(string)
