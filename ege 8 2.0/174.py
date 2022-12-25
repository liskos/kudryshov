a = set()
for s1 in "КАЛИ":
    for s2 in "КАЛИЙ":
        for s3 in "КАЛИЙ":
            for s4 in "КАЛИЙ":
                for s5 in "КАЛИЙ":
                    for s6 in "КАЛИ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("Й") <= 1 and s.count("ИЙ") == 0 and s.count("ИЕ") == 0 :
                            a.add(s)
print(len(a))
print(a)
