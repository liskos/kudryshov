k = 0
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                for s5 in "01234567":
                    f = s1 + s2 + s3 + s4 + s5
                    f1 = f.replace("0","h").replace("2","h").replace("4","h").replace("6","h")
                    if f.count("4") == 1 and ("hh" not in f1):
                        k += 1
                        print(k, f)

