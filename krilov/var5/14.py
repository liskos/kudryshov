def f(n):
    s =""
    while n > 0:
        s += str(n % 5)
        n = n // 5
    return s[::-1]

x = 5 ** 2022 - 2 * 5 ** 1010 + 25 ** 850 + 2500
print(f(x).count("4"))
