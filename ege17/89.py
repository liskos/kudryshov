def f(n):
    s1 = str(n)[:2]
    s2 = str(n)[-2:]
    s = abs(int(s1) - int(s2))
    return s

a = []
for i in range(1234567,7654321 + 1):
    if f(i) != 0 and i % f(i) == 0:
        a.append(i)

print(len(a),max(a))

