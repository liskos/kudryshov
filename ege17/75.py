b = []
m = 0
for i in range(138, 603884 + 1):
    a = i
    if len(set(str(i))) < len(str(i)) and i ** (1/3) == int(i ** (1/3)):
        b.append(i)
        if (sum(map(int,str(a)))) > (sum(map(int,str(m)))):
            m = a
print(len(b),m)
