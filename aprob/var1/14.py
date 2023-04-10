x = 2 * 729 ** 1021  - 2 * 243 ** 1022 + 81 ** 1023 - 2 * 27 ** 1024 - 1025
def f(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]
s = f(x)

print(f(x))
print(s.count("0"))
