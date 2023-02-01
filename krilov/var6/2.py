for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = (not(not z or y) or x) or not w
                if int(f) < 1 :
                    print(w,y,z,x,"|", int(f))
