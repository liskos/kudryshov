for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not z and x) or (x and y)
            print(z,y,x, "|", int(f))
