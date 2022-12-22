i = 0
for s1 in "АКЛОШ":
    for s2 in "АКЛОШ":
        for s3 in "АКЛОШ":
            for s4 in "АКЛОШ":
                for s5 in "АКЛОШ":
                    s = s1 + s2 + s3 + s4 + s5
                    i += 1
                    if s == "ШКОЛА":
                        print(i,s)
