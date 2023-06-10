alf = 'ХОЧУНАБЮДЖЕТ'
gl = "ОУАЮЕ"
b = []
k = 0
for a1 in "ОУАЮЕ":
    for a2 in "ОУАЮЕ":
        for a3 in "ОУАЮЕ":
            for a4 in "ОУАЮЕ":
                for a5 in "ОУАЮЕ":
                    a = a1 + a2 + a3 + a4 + a5
                    if len(set(a)) == 5:
                        b.append(a)

for s1 in 'ХОЧУНАБЮДЖЕТ':
    for s2 in 'ХОЧУНАБЮДЖЕТ':
        for s3 in 'ХОЧУНАБЮДЖЕТ':
            for s4 in 'ХОЧУНАБЮДЖЕТ':
                for s5 in 'ХОЧУНАБЮДЖЕТ':
                    s = s1 + s2 + s3 + s4 + s5
                    for i in range(120):
                        if b[i] not in s:
                            k+=1


print(k)

