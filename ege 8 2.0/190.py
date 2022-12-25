a = set()
for s1 in "КАЛЬ":
    for s2 in "КАЛЬ":
        for s3 in "КАЛЬ":
            for s4 in "КАЛЬ":
                for s5 in "КАЛЬ":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("А") <= 1  :
                        a.add(s)
print(len(a))
print(a)
