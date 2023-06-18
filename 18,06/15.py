for a in range(1,1000):
    if all(((x % 17 != 0) or ((x not in range(80,100+1)) or (a<(x+30)))) for x in range(1,1000)):
        print(a)