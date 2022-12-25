a = set()
for s1 in "ВОРБЕ":
    for s2 in "ВОРБЕЙ":
        for s3 in "ВОРБЕЙ":
            for s4 in "ВОРБЕЙ":
                for s5 in "ВОРБЕ":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("Й") <= 1 and s.count("ЕЙ") == 0 and s.count("ЙЕ") == 0 :
                     a.add(s)
print(len(a))
print(a)
