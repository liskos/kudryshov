k = 0
for s1 in "ABCD":
    for s2 in "ABCD":
        for s3 in "ABCD":
            for s4 in "ABCD":
                s = s1 + s2 + s3 + s4
                if s.count("A") == 2:
                    k += 1
                    print(k,s)

