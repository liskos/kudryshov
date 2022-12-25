a = set()
for s1 in "СОЛВЕ":
    for s2 in "СОЛВЕЙ":
        for s3 in "СОЛВЕЙ":
            for s4 in "СОЛВЕЙ":
                for s5 in "СОЛВЕЙ":
                    for s6 in "СОЛВЕ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("Й") <= 1 and s.count("ЕЙ") == 0 and s.count("ЙЕ") == 0 :
                            a.add(s)
print(len(a))
print(a)
