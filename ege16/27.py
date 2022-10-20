def f(n):
    k = (n+1)
    if n > 1 :
       k += 2 * n
       k += f(n - 1)
       k += f(n-3)
    return k

for i in range (1,999):
    if f(i) > 100000:
        print(i)
        print(f(i))
        break
