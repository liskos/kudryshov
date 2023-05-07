def f(n):
    if n == 998:
        return 1495506
    if n == 1995:
        return 5973033
    if n == 1:
        return 6
    if n > 1 :
        return 3*n + f(n-1)
print(f(1995))
print((f(2023) - f(1984)))