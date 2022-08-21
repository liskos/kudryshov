def f(s):
    n = 0
    while s > 0 :
        s = s - 5
        n = n + 2
    return n


for i in range(999,1,-1):
    if f(i) == 150:
     print(i)
     break