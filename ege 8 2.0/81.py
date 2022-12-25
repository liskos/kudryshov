i = 0
for s1 in "АВГДИНОР":
    for s2 in "АВГДИНОР":
        for s3 in "АВГДИНОР":
            for s4 in "АВГДИНОР":
                s = s1 + s2 + s3 + s4
                i += 1
                if s1 == "Г" and s2 == "О":
                    print(i, s)
