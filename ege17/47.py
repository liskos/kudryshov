a = []
b = []
for i in range(2055, 9414 + 1):
    if ((i % 10) + (i // 10 % 10) !=5) and (i % 4 != 0) and (i % 5 != 0) and (i % 41 != 0):
        a.append(i)
        b.append(i % 1000)
print(len(a), min(a))
s = 1
for i in b:
    s = s * i
print(s)
