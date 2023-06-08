def f(n):
    s = []
    while n > 0:
        s.append(n % 16)
        n = n // 16
    return s[::-1]


a = []
for i in range(333,11223+1):
    if (i % 16 == 11) and f(i)[0] == 12 and (i % 6 != 0):
        a.append(i)

print(len(a),max(a))