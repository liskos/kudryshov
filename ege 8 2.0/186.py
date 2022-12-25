a = set()
for s1 in "БАЛОН":
    for s2 in "БАЛОН":
        for s3 in "БАЛОН":
            for s4 in "БАЛОН":
                for s5 in "БАЛОН":
                    for s6 in "БАЛОН":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("А") <= 1 and s.count("О") <= 1 :
                            a.add(s)
print(len(a))
print(a)
