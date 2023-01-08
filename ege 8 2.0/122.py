a = set()
for s1 in "МОЛК":
    for s2 in "МОЛК":
        for s3 in "МОЛК":
            for s4 in "МОЛК":
                for s5 in "МОЛК":
                    for s6 in "МОЛК":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("О") == 3 and len(set(s)) == 4:
                            a.add(s)
print(len(a))


