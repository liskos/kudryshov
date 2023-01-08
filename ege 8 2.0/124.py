a = set()
for s1 in "ЧИУА":
    for s2 in "ЧИУА":
        for s3 in "ЧИУА":
            for s4 in "ЧИУА":
                for s5 in "ЧИУА":
                    for s6 in "ЧИУА":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("У") == 2 and s.count("А") == 2 and len(set(s)) == 4:
                            a.add(s)
print(len(a))


