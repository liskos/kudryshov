a = set()
for s1 in "ОБЕМ":
    for s2 in "ОБЪЕМ":
        for s3 in "ОБЪЕМ":
            for s4 in "ОБЕМ":
                s = s1 + s2 + s3 + s4
                if s.count("О") == 1 :
                    a.add(s)
print(len(a))
print(a)
