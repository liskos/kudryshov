a = set()
for s1 in "ABC":
    for s2 in "ABC":
        for s3 in "ABC":
            for s4 in "ABC":
                for s5 in "ABCX":
                    s = s1 + s2 + s3 + s4 + s5
                    a.add(s)

print(len(a))
print(a)



