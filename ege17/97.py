def f(n):
    s = []
    while n > 0:
        s.append(n % 16)
        n = n // 16
    return s[::-1]


a = []
for i in range(777,3777+1):
    if (i % 16 == 15) and f(i)[0] == 10 and (i % 11 != 0):
        a.append(i)

print(len(a),max(a))