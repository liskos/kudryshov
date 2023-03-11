k = 0
for s1 in "123456":
    for s2 in "123456":
        for s3 in "123456":
            for s4 in "123456":
                for s5 in "123456":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("1") == 1:
                        k += 1
print(k)
