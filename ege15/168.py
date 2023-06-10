for a in range(1,1000):
    if all((not((x & 28 != 0) or (x & 45 !=0)) or not((x & 17 == 0) or (x in a != 0)))for x in range(1,1000)):
        print(a)
        break