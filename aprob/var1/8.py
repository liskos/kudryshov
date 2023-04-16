k = 0
b = []
for s1 in "АЙКОС":
    for s2 in "АЙКОС":
        for s3 in "АЙКОС":
            for s4 in "АЙКОС":
                for s5 in "АЙКОС":
                    s = s1 + s2 + s3 + s4 + s5
                    k += 1
                    if s.count("О") <= 1 and "СС" not in s:
                       print(s,k)




