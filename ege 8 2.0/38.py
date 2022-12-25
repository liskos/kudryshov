i = 0
for s1 in "АОУ":
    for s2 in "АОУ":
        for s3 in "АОУ":
            for s4 in "АОУ":
                for s5 in "АОУ":
                    s = s1 + s2 + s3 + s4 + s5
                    i += 1
                    if s == "УАУАУ":
                        i1 = i
                    if s == "ОУОУА":
                        i2 = i
print(i1, i2)
print(i1 - i2 + 1)
