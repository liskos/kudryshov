def f(n):
    if n <= 1:
        return 3
    if n > 1:
        return f(n-1) + 2 * f(n-2) -5


print(f(22))
