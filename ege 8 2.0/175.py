i = 0
for s1 in "ВКНСТ":
    for s2 in "АВИКНСТ":
        for s3 in "АВИКНСТ":
            for s4 in "АИ":
                i += 1
                s = s1 + s2 + s3 + s4
                print(i,"|", s)
