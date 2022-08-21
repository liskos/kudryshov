def f(s):
    n = 0
    while s > 0 :
        s = s - 20
        n = n + 3
    return n


for i in range(1,999):
    if f(i) == 48:
     print(i)
     break