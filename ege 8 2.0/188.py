a = set()
for s1 in "САКУР":
    for s2 in "САКУР":
        for s3 in "САКУР":
            for s4 in "САКУР":
                for s5 in "САКУР":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("А") <= 1 and s.count("У") <= 1 :
                        a.add(s)
print(len(a))
print(a)
