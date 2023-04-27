from functools import lru_cache

@lru_cache()
def f(n):
    if n == 10**200:
        return 1
    if n == 10**500:
        return 1
    if n == 10**998:
        return 1
    if n < 10:
        return n
    else :
        return n % 10 + f(n//10)

print(f(10**998 + 12345))