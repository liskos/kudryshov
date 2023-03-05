s = []
for x in range(1,9999):
    for y in range(1,9999):
        for a in range(1,99999):
            f = (x >= a) or (y >= a) or (x * y <= 200)
            if int(f) == 1:
                s.append(a)
            print(max(s))