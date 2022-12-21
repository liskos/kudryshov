i = 0
k = 0
m = 0
for s1 in "OПРТ":
    for s2 in "OПРТ":
        for s3 in "OПРТ":
            for s4 in "OПРТ":
                for s5 in "OПРТ":
                    s = s1 + s2 + s3 + s4 + s5
                    i += 1
                    if s == 'РОПОТ':
                        k += i
                    if s == 'ТОПОР':
                        m += i

                    print(i,'|', s)
print('---------')
print(k)
print(m)



