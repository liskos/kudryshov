a = set()
for s1 in "САЛЬ":
    for s2 in "САЛЬ":
        for s3 in "САЛЬ":
            for s4 in "САЛЬ":
                for s5 in "САЛЬ":
                    for s6 in "САЛЬ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("А") <= 1  :
                            a.add(s)
print(len(a))
print(a)
