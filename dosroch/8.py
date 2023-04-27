k = 0
for s1 in "РСКЫНИ":
    for s2 in "РСКЫНИ":
        for s3 in "РСКЫНИ":
            for s4 in "РСКЫНИ":
                for s5 in "РСКЫНИ":
                    for s6 in "РСКЫНИ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        k += 1
                        if s == "СЫРСЫР":
                            print(s,k)
                        if s == "СЫРНИК":
                            print(s,k)