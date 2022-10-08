def f(n):
    if n == 21:
        return 946
    if n == 20:
        return 6765
    if n == 0:
        return 0
    if 0 < n < 3:
        return 1
    if n >= 3:
        return (f(n-2) + f(n-1)) % 10000

print(f(47))