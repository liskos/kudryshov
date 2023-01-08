a = set()
for s1 in "ТАР":
    for s2 in "ТАР":
        for s3 in "ТАР":
            for s4 in "ТАР":
                for s5 in "ТАР":
                    for s6 in "ТАР":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("А") == s.count("Т") == s.count("Р") == 2:
                            a.add(s)
print(len(a))


