a = set()
for s1 in "KRANT":
    for s2 in "KRANT":
        for s3 in "KRANT":
            for s4 in "KRANT":
                for s5 in "KRANT":
                        s = s1 + s2 + s3 + s4 + s5
                        if s.count("K") == 2:
                            a.add(s)
print(len(a))
print(a)