a = set()
for s1 in "НОБЕЛИЙ":
    for s2 in "НОБЕЛИЙ":
        for s3 in "НОБЕЛИЙ":
            for s4 in "НОБЕЛИЙ":
                for s5 in "НОБЕЛИЙ":
                    for s6 in "НОБЕЛИЙ":
                        for s7 in "НОБЕЛИЙ":
                            s = s1 + s2 + s3 + s4 + s5 + s6 + s7
                            if s1 != "Й" and "ИЙО" not in s and len(set(s)) == 7:
                                a.add(s)
print(len(a))
print(a)
