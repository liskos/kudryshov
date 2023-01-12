a = set()
for s1 in "МАРИ":
    for s2 in "МАРИ":
        for s3 in "МАРИ":
            for s4 in "МАРИ":
                for s5 in "ИНА":
                    for s6 in "ИНА":
                        for s7 in "ИНА":
                            for s8 in "ИНА":
                                s = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
                                if len(set([s1,s2,s3,s4])) == 4:
                                    a.add(s)
c = list(a)
c.sort()
print(c.index("МАРИАННА"))


