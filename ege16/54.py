def f(n):
    if n > 25:
        return 2 * n * n * n + n * n
    if n <= 25:
        return f(n+2) + 2 * f(n+3)

s = f(2)
print(sum(map(int,str(s))))