a = set()
for s1 in "KANT":
    for s2 in "KANT":
        for s3 in "KANT":
            for s4 in "KANT":
                for s5 in "KANT":
                    for s6 in "KANT":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("K") == 2:
                            a.add(s)
print(len(a))
print(a)