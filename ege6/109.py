def f(s):
    n = 400
    while s - n > 0:
        s = s - 20
        n = n - 15
    return s


for i in range(1,999):
    if f(i) < 0 :
        print(i)
        break
        