a = set()
for s1 in "СЧИТАЙ":
    for s2 in "СЧИТАЙ":
        for s3 in "СЧИТАЙ":
            for s4 in "СЧИТАЙ":
                s = s1 + s2 + s3 + s4
                if s.count("А") <= 1 :
                    a.add(s)
print(len(a))
print(a)
