def f(n):
    if n > 15:
        return n * n - 5
    if n <= 15:
        return n * f(n+2) + n + f(n+3)

s = f(1)
print(f(1))
print(sum(map(int,str(s))))