def f(n):
    if n == 20:
        return 45
    if n == 30:
        return 65
    if n == 0 :
        return 1
    if n > 0 :
        return 2 * f(1-n) + 3 * f(n-1) + 2
    if n < 0:
        return -f(-n)

print(f(50))