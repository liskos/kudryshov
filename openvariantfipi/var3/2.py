for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or (not y)) and (not(y == z)) and (not w)
                if f:
                    print(x,z,y,w,"|",int(f))