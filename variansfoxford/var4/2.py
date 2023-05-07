for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (not x or z) and (not(not y or w)) and (not w )
                if f:
                    print(y,z,x,w,"|",int(f))
