for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (not(not w or x)) or (z or not y) or z
                if not f:
                    print(w,z,x,y)
