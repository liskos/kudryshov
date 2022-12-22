a = set()
for s1 in "КОТ":
    for s2 in "КОТ":
        for s3 in "КОТ":
            for s4 in "КОТ":
                for s5 in "КОТ":
                    for s6 in "КОТ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count('К') == 2:
                            a.add(s)
print(len(a))
print(a)



