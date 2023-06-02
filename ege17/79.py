def d(n):
    a = []
    for i in range(1,int(n ** 0.5) +1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return len(set(a)) == 2

b =[]
c = []
for i in range(2095,19402):
    if d(i) and str(i)[0] > str(i)[-1]:
        b.append(i)
        if str(i)[-2:] == "21":
            c.append(i)
print(len(b))
print(max(c))