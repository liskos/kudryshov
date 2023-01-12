k = 0
for s2 in "01234":
    for s3 in "01234":
        for s4 in "01234":
            for s5 in "01234":
                for s6 in "01234":
                    s = "3" + s2 + s3 + s4 + s5 + s6
                    x = int(s,5)
                    if x % 2 == 0 :
                        k +=1
print(k)
