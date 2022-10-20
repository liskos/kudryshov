def f(n):
    k = 2 * n + 1
    if n > 1 :
       k += 3 * n - 8
       k += f(n - 1)
       k += f(n-4)
    return k

for i in range (1,999):
    if f(i) > 500000:
        print(i)
        print(f(i))
        break
