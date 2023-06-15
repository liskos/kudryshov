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
                    for s6 in 'ХОЧУНАБЮДЖЕТ':
                        for s7 in 'ХОЧУНАБЮДЖЕТ':
                            for s8 in 'ХОЧУНАБЮДЖЕТ':
                                for s9 in 'ХОЧУНАБЮДЖЕТ':
                                    for s10 in 'ХОЧУНАБЮДЖЕТ':
                                        for s11 in 'ХОЧУНАБЮДЖЕТ':
                                            for s12 in 'ХОЧУНАБЮДЖЕТ':
                                                s = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12
                                                if all(i not in s for i in b):
                                                     k+=1


print(k)

