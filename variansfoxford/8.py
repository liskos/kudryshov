k = 0
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                for s5 in "01234567":
                    s = s1 + s2 + s3 + s4 + s5
                    ss = s.replace("0","C")
                    ss = ss.replace("2", "C")
                    ss = ss.replace("4", "C")
                    ss = ss.replace("6", "C")
                    ss = ss.replace("1", "N")
                    ss = ss.replace("3", "N")
                    ss = ss.replace("5", "N")
                    ss = ss.replace("7", "N")
                    if s.count("5") == 1 and "NN" not in ss:
                        k += 1
print(k)
