def f(s):
    n = 80
    while s + n < 160 :
        s = s + 15
        n = n - 10
    return s

for i in range(1,999):
    if f(i) <= 100:
        print(i)
        break