for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((not x or y) or (not w == z))
                d = ((not x or y) == (w and not z))
                if f == d:
                    print(w,y,x,z)
