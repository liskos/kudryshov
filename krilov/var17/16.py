def f(n):
    if n == 100:
        return 338350
    if n == 500:
        return 41791750
    if n == 1000:
        return 333833500
    if n == 1500:
        return 1126125250
    if n == 1 :
        return 1
    if n > 1:
        return n ** 2 + f(n-1)

print(f(2023) - f(2019))