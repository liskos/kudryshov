for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = not(not x or z) and (not w or y) and not z
                if int(f) > 0 :
                    print(z,w,y,x,"|",int(f))