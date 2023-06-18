k = 0
for s1 in "АВЛОР":
    for s2 in "АВЛОР":
        for s3 in "АВЛОР":
            for s4 in "АВЛОР":
                s = s1 + s2 + s3 + s4
                k += 1
                if s1 == "Л":
                    print(k,s)
                    break
