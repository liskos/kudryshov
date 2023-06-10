k = 0
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                for s5 in "01234567":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("6") == 1 and "16" not in s and "61" not in s and "36" not  in s and "63" not in s and \
                            "56" not in s and "65" not in s and "76" not in s and "67" not in s and "69" not in s and "96" not in s:
                        k+=1

print(k)

