def f(n):
    if n < 0:
        return n * -1
    if n >= 0 and n % 2 == 0 :
        return 2 * n + 1 + f(n-3)
    if n >= 0 and n % 2 != 0 :
        return 4 * n + f(n - 4)

print(f(33))