def f(n):
    k = n**2
    if n > 1 :
        k += 2 * n + 1
        k += f(n-2)
        k += f(n//3)
    return k

for i in range(1,999):
    if f(i) > 3200000:
        print(i)
        print(f(i))
        break