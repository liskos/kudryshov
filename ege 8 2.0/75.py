a = set()
c = "KRBL"
g = "OAI"
for s1 in c:
    for s2 in g:
        for s3 in c:
            for s4 in g:
                for s5 in c:
                    for s6 in g:
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if len(set(s)) == 6:
                            a.add(s)
print(a)
print(len(a))

