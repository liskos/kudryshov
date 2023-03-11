k = 0
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                s = s1 + s2 + s3 + s4
                if len(set(s)) == 3 and ((s1 == s2) or (s2 == s3) or (s3 == s4)):
                    k += 1
print(k)
