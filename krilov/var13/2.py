for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (((x == (not y)) or (x == (not z))) and w and (not y or z))
                if f:
                    print(x,y,z,w,"|", int(f))

