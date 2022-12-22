i = 0
a = set()
for s1 in "ABCDX":
    for s2 in "ABCDX":
        for s3 in "ABCDX":
            for s4 in "ABCDX":
                s = s1 + s2 + s3 + s4
                if s.count("X") == 1:
                    a.add(s)
print(len(a))
print(a)

