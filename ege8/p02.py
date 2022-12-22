i = 0
for s1 in "КЛРТ":
    for s2 in "КЛРТ":
        for s3 in "КЛРТ":
            for s4 in "КЛРТ":
                s = s1 + s2 + s3 + s4
                i += 1
                if i == 67:
                    print (i,s)
