i = 0
for s1 in "АГИЛМОРТ":
    for s2 in "АГИЛМОРТ":
        for s3 in "АГИЛМОРТ":
            for s4 in "АГИЛМОРТ":
                s = s1 + s2 + s3 + s4
                i += 1
                if s3 == "А" and s4 == "Л":
                    print(i, s)
