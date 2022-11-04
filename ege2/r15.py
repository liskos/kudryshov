for z in 0,1:
    for y in 0, 1:
        for x in 0, 1:
            f = (x or not y or not z) and (not x or y)
            if not f:
             print(z,y,x, '|', int(f))
