def f(n):
    if n == 20:
        return 70841
    if n == 21:
        return 114625
    k = 1
    if n >= 1 :
        k += 1
        k += f(n-1)
        k += f(n-2)
        k += 1
    return k

print(f(35))