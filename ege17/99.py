def f(n):
    s = []
    while n > 0:
        s.append(n % 16)
        n = n // 16
    return s[::-1]


a = []
for i in range(100,1000000+1):
    if (i % 16 == 10) and f(i)[0] == 11 and (i % 12 != 0):
        a.append(i)

print(len(a),max(a))