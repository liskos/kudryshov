a = set()
for s1 in "АКШОЛ":
    for s2 in "АКШОЛ":
        for s3 in "АКШОЛ":
            for s4 in "АКШОЛ":
                for s5 in "АКШОЛ":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("А") > 0 or s.count("О") > 0 :
                     a.add(s)
print(len(a))
print(a)
