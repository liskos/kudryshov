i = 0
for s1 in "АИОУЭ":
    for s2 in "АИОУЭ":
        for s3 in "АИОУЭ":
            for s4 in "АИОУЭ":
                for s5 in "АИОУЭ":
                    for s6 in "АИОУЭ":
                        i += 1
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        print(i,"|", s)
