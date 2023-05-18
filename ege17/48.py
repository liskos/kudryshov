a = []
b = []
for i in range(1985, 8528 + 1):
    if ((i % 10) + (i // 10 % 10) ==6) and (i % 2 != 0) and (i % 7 != 0) and (i % 47 != 0):
        a.append(i)
        b.append(i % 1000)
print(len(a), max(a))
s = 1
for i in b:
    s = s * i
print(s)
