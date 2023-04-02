k = 0
for s1 in ("abc"):
    for s2 in ("abc"):
        for s3 in ("abc"):
            for s4 in ("abc"):
                for s5 in ("abc"):
                    for s6 in ("abc"):
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count("a") == 1 :
                            k+=1
                            print(k,s)
