a = set()
for s1 in "каркас":
    for s2 in "каркас":
        for s3 in "каркас":
            for s4 in "каркас":
                for s5 in "каркас":
                    for s6 in "каркас":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("к") + s.count("р") + s.count("с") >= 3 :
                            a.add(s)
print(len(a))
