k = 0
for s1 in "АКМСУ":
    for s2 in "АКМСУ":
        for s3 in "АКМСУ":
            for s4 in "АКМСУ":
                for s5 in "АКМСУ":
                    s = s1 + s2 + s3 + s4 + s5
                    k += 1
                    if "КУМАС" in s:
                        print(k,s)
