a = set()
for s1 in "ТРАТАТА":
    for s2 in "ТРАТАТА":
        for s3 in "ТРАТАТА":
            for s4 in "ТРАТАТА":
                for s5 in "ТРАТАТА":
                    for s6 in "ТРАТАТА":
                        for s7 in "ТРАТАТА":
                            s = s1 + s2 + s3 + s4 + s5 + s6 + s7
                            if s.count("А") == 3 and s.count("Т") == 3 and len(set(s)) == 3:
                                a.add(s)
print(len(a))


