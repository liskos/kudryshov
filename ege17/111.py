def f(n):
    s = []
    while n > 0:
        s.append(n % 5)
        n = n // 5
    return set(s)

a = []
for i in range(10,6000+1):
    if len(f(i)) == 1 and  and i % 6 == 0:
        a.append(i)

print(len(a),sum(a))

print(f(600))