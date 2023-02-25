def f(n):
    if n == 100:
        return 10103
    if n == 500:
        return 250503
    if n == 1000:
        return 1001003
    if n == 1500:
        return 2251503
    if n == 2000:
        return 4002003
    if n == 1 :
        return 5
    if n > 1 :
        return 2 * n + f(n-1)

print(f(2048) - f(1024))