a = set()
for s1 in "ЖАЛЕ":
    for s2 in "ЖАЛЕЙ":
        for s3 in "ЖАЛЕЙ":
            for s4 in "ЖАЛЕЙ":
                for s5 in "ЖАЛЕ":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("Й") <= 1 and s.count("ЕЙ") == 0 and s.count("ЙЕ") == 0 :
                     a.add(s)
print(len(a))
print(a)
