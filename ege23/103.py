def f(a,b):
    k = 0
    if a == b:
        k += 1
        return 1
        return k
    if a > b :
        return 0
    return f(a + 1,b) + f(a + 2,b) + f(a * 2,b)


print(f(1,20))
print(k)