import math

i = int(input("Enter your angle of incidence: "))
r = int(input("Enter your angle of refraction: "))

top = round(math.sin(i), 2)
bottom = round(math.sin(r), 2)
answer = top / bottom
print(round(answer, 2))
