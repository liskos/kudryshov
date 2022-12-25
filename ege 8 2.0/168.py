a = set()
for s1 in "КЛЕ":
    for s2 in "КЛЕЙ":
        for s3 in "КЛЕЙ":
            for s4 in "КЛЕЙ":
                for s5 in "КЛЕЙ":
                    for s6 in "КЛЕ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("Й") <= 1 and s.count("ЕЙ") == 0 and s.count("ЙЕ") == 0 :
                            a.add(s)
print(len(a))
print(a)
