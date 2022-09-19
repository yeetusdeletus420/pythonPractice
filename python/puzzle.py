for i in range(0,299999):
    x = 99999
    x = x + 1
    y = str(x)
    z = str(x*2)
    if y in z:
        print(x)
    else:
        continue
