a = set()
for s1 in "MAPT":
    for s2 in "MAPT":
        for s3 in "MAPT":
            for s4 in "MAPT":
                for s5 in "MAPT":
                    for s6 in "MAPT":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count('P') == 2:
                            a.add(s)

print(len(a))  
print(a)
