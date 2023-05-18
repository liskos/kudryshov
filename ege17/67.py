b = []
for i in range(100001, 900009 + 1):
    s = i % 10
    if ((s % 7) + s == 10) and ((i % 11 == 0) and (i % 55 != 0)):
        b.append(b)

print(max(b),len(b))
