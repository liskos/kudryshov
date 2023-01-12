a = set()
for s1 in "РУСТАМ":
    for s2 in "РУСТАМ":
        for s3 in "РУСТАМ":
            for s4 in "РУСТАМ":
                for s5 in "РУСТАМ":
                    for s6 in "РУСТАМ":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("Р") + s.count("С") + s.count ("Т") + s.count("М") >= 3 :
                            a.add(s)
print(len(a))
