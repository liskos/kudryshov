for a in range(1,1000):
    if all(not(x & 76 != 0) or (not(x & 10 == 0 ) or (x & a != 0))for x in range(1,1000)):
        print(a)
        break