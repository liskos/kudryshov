a = set()
for s1 in "ЗАПИС":
    for s2 in "ЗАПИСЬ":
        for s3 in "ЗАПИСЬ":
            for s4 in "ЗАПИСЬ":
                for s5 in "ЗАПИСЬ":
                    for s6 in "ЗАПИСЬ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("АЬ") == 0 and s.count("ИЬ") == 0 :
                            a.add(s)
print(len(a))
print(a)
