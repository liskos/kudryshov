def f(n):
    if n > 25 :
        return n * n + 2 * n + 1
    if n <= 25 and n % 2 == 0 :
        return 2 * f(n+1) + f(n+3)
    if n <= 25 :
        return f(n+2) + 3 * f(n+5)

