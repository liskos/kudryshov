def f(n):
    if n > 25:
        return 2 * n * n * n + 1
    if n <= 25:
        return f(n+2) + 2 * f(n+3)

print(f(2))