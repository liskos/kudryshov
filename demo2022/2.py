for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not(not y or x) or(not z or w) or not z
                if not f:
                    print(y,x,z,w)
