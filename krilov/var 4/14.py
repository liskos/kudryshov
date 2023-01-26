def f(n):
    s = []
    while n > 0:
        s.append(n % 11)
        n = n // 11
    return s[::-1]


x = 1331 ** 650 - 55 * 121 ** 610 + 77 * 11 ** 510 - 3 * 11 ** 100 - 221
print(f(x).count(10))