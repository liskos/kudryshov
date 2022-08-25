def f(s):
    n = 0
    while s < s * s :
        s = s - 1
        n = n + 3
    return n

for i in range(1,999):
    if f(i) > 2000 :
        print(i)
        break