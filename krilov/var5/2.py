for x in 0,1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = not(not(not x or y) or w) and z
                if int(f) > 0:
                    print(w, y, x, z, "|", int(f))

