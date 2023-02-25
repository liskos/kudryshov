k = 0
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                for s5 in "01234567":
                    f = s1 + s2 + s3 + s4 + s5
                    if f.count("4") == 1 and ("24" not in f) and ("26" not in f) and ("46" not in f) and ("42" not in f) and ("62" not in f) and ("64" not in f):
                        k += 1
                        print(k, f)

