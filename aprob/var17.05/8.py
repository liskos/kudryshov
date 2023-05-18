k = 0
for s1 in "АВОРТ":
    for s2 in "АВОРТ":
        for s3 in "АВОРТ":
            for s4 in "АВОРТ":
                for s5 in "АВОРТ":
                    for s6 in "АВОРТ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        k += 1
                        if "ВОРОТА" in s:
                            print(k,s)

