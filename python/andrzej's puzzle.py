a = 100000

for i in range(0,1000000):
    
    x = a + 1
    y = str(x)
    z = str(y)

    if y in z:
        print(x)
        break
    else:
        continue
