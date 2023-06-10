from functools import lru_cache

@lru_cache (maxsize=None)
def f(n):
    if n >= 3210:
        return 1
    if n < 3210:
        return f(n+3) + 7

@lru_cache (maxsize=None)
def g(n):
    if n < 10:
        return n
    if n > 10:
        return g(n-3)

print(f(15)-9)