for a in range(1,1400):
    if all((not(x & 56 != 0) or (not(x & 48 == 0) or (x & a != 0))) for x in range(1,1400)):
        print(a)