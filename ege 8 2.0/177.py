a = set()
for s1 in "ДЖОБС":
    for s2 in "ДЖОБС":
        for s3 in "ДЖОБС":
            for s4 in "ДЖОБС":
                for s5 in "ДЖОБС":
                    for s6 in "ДЖОБС":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("Д") == 1 and s.count("О") == 1 and s.count("С") == 1 and s.count("Ж") <= 2:
                            a.add(s)
print(len(a))
print(a)
