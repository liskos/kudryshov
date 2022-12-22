a = set()
for s1 in "KROT":
    for s2 in "KROT":
        for s3 in "KROT":
            for s4 in "KROT":
                for s5 in "KROT":
                    for s6 in "KROT":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("O") == 1:
                            a.add(s)
print(len(a))
print(a)