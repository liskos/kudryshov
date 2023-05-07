for a in range(1,100):
    for x in range(1,100):
        f = ((x % 3 != 0) or  (x % 11 != 0 )) or (x + a >= 80)
        if f:
            print(a,x)