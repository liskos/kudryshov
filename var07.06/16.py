def f(n):
    if n == 2182:
        return 1
    if n < 3:
        return 2
    if n > 2:
        return 2 * f(n-2)

print(f(2222) / f(2182))