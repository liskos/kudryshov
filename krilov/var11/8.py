k = 0
for s1 in "0123":
    for s2 in "0123":
        for s3 in "0123":
            s = s1 + s2 + s3
            if int(s1) >= int(s2) >= int(s3):
                k += 1
                print(s,k)

