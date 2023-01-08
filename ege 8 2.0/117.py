a = set()
for s1 in "КБАЛ":
    for s2 in "КБАЛ":
        for s3 in "КБАЛ":
            for s4 in "КБАЛ":
                for s5 in "КБАЛ":
                    for s6 in "КБАЛ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if len(set(s)) == 4 and s.count("А") == 3 and "АА" not in s:
                            a.add(s)
print(len(a))
