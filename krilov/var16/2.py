for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not((x == y) or (x == w)) or z or (not(not y or w))
                if not f:
                    print(w,y,x,z)
