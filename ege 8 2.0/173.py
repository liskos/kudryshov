a = set()
for s1 in "ЕЛ":
    for s2 in "ЕЛЙ":
        for s3 in "ЕЛЙ":
            for s4 in "ЕЛЙ":
                for s5 in "ЕЛЙ":
                    for s6 in "ЕЛ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("Й") <= 1 and s.count("ЕЙ") == 0 and s.count("ЙЕ") == 0 :
                            a.add(s)
print(len(a))
print(a)
