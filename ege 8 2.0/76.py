a = set()
g = "ОАИ"
c = "КРБЛ"
for s1 in g:
    for s2 in c:
        for s3 in g:
            for s4 in c:
                for s5 in g:
                    s = s1 + s2 + s3 + s4 + s5
                    if len(set(s)) == 5:
                        a.add(s)
print(len(a))
print(a)


