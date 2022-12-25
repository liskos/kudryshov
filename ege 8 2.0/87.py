a = set()
i = 0
for s1 in "ВЕКНО":
    for s2 in "ВЕКНО":
        for s3 in "ВЕКНО":
            for s4 in "ВЕКНО":
                for s5 in "ВЕКНО":
                    s = s1 + s2 + s3 + s4 + s5
                    i += 1
                    if s.count("Н") == 1 and s.count("К") == 1:
                        a.add(s)
print(len(a))
print(a)
