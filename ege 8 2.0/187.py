a = set()
for s1 in "БАНКИР":
    for s2 in "БАНКИР":
        for s3 in "БАНКИР":
            for s4 in "БАНКИР":
                for s5 in "БАНКИР":
                    for s6 in "БАНКИР":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("А") <= 1 and s.count("И") <= 1 :
                            a.add(s)
print(len(a))
print(a)
