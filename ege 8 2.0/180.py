a = set()
for s1 in "МЕЧТА":
    for s2 in "МЕЧТА":
        for s3 in "МЕЧТА":
            for s4 in "МЕЧТА":
                for s5 in "МЕЧТА":
                    for s6 in "МЕЧТА":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("А") >= 3 :
                            a.add(s)
print(len(a))
print(a)
