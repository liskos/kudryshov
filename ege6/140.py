def f(s):
    n = 10
    while s - n < 1000:
        s = s + n
        n = n + 5
    return n

k = 0
for i in range(1,999):
    if f(i) == 80:
        k += 1
    print(k)