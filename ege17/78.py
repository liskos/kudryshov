def f(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] <= n[i + 1]:
            return False
    return True

def d(n):
    a = []
    for i in range(1,int(n ** 0.5) +1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return len(set(a)) % 3 == 0

b = []
c = []
for i in range(1082,129932 + 1):
    if f(i) and d(i):
        b.append(i)
        if str(i)[0] == "7":
            c.append(i)

print(len(b))
print(max(c))


