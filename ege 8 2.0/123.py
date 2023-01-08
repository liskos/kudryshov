a = set()
for s1 in "АСИН":
    for s2 in "АСИН":
        for s3 in "АСИН":
            for s4 in "АСИН":
                for s5 in "АСИН":
                    for s6 in "АСИН":
                        for s7 in "АСИН":
                            s = s1 + s2 + s3 + s4 + s5 + s6 + s7
                            if s.count("С") == 3 and s.count("А") == 2 and len(set(s)) == 4:
                                a.add(s)
print(len(a))


