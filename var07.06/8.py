k = 0
for s1 in "АЕКНС":
    for s2 in "АЕКНС":
        for s3 in "АЕКНС":
            for s4 in "АЕКНС":
                for s5 in "АЕКНС":
                    for s6 in "АЕКНС":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        k += 1
                        if "СЕНЕКА" in s:
                            print(k,s)
