def f(n):
    if n > 30:
        return n * n + 5 + 4
    if n <= 30 and n % 2 == 0 :
        return f(n+1) + 4 * f(n+4)
    if n <= 30 and n % 2 !=0:
        return 2 * f(n+2) + f(n + 5)

