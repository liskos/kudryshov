for a in range(0,1000):
    if all((x & 39 == 0 or ((x & 11 != 0) or(x & a != 0))) for x in range(0,1000)):
        print(a)