for a in range(1,99999):
    s = []
    for x in range(1,400):
        for y in range(1,400):
            f = (x >= a) or (y >= a) or (x * y <= 200)
            s.append(f)
    if all(s):
        print(a)