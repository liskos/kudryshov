from functools import lru_cache
@lru_cache()
def f(n):
    if n == 500:
        return 3145709441951010018970409318287906920014663976925402173410621501352876222631088276177605154484952886588124
    if n == 1 :
        return 1
    if n == 2:
        return 2
    if n > 2 :
        return n * (n-1) + f(n-1) + f(n-2)
print(f(400))
print(f(2023)- f(2021) + 2 * f(2020) - f(2019))