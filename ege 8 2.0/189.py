a = set()
for s1 in "КОРНЕТ":
    for s2 in "КОРНЕТ":
        for s3 in "КОРНЕТ":
            for s4 in "КОРНЕТ":
                for s5 in "КОРНЕТ":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("О") <= 1 and s.count("Е") <= 1 :
                        a.add(s)
print(len(a))
print(a)
