def f(n):
    if n % 2 == 0:
        n = n // 2
    else :
        n = n - 1
    if n % 3 == 0 :
        n = n // 3
    else:
        n = n - 1
    if n % 7 == 0:
        n = n // 7
    else :
        n = n - 1
    return n

k = 0
for i in range(1,999):
    if f(i) == 2:
        k+=1
print(k)