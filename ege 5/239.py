def f(n):
    s = ""
    while n > 0:
        s += str(n % 6)
        n = n // 6
    return s[::-1]


def alg(k):
    k = f(k)
    k = k + k[-1]
    k = int(k, 6)
    k = bin(k)[2:]
    k = k + k[-1]
    return int(k, 2)


m = 0
for i in range(1, 999):
    if alg(i) < 344:
        m = max(m, alg(i))
print(m)
