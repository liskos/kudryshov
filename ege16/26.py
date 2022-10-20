def f(n):
    k = (n+1)
    if n > 1 :
       k += (n + 5)
       k += f(n - 1)
       k += f(n-2)
    return k

for i in range (1,999):
    if f(i) > 1000000:
        print(i)
        print(f(i))
        break
