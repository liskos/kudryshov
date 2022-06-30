def f(d):
    n = 5
    s = 83
    while s <= 1200 :
        s = s + d
        n = n + 6
    return n


for i in range (1, 9999):
    if f(i) == 89:
        print(i)



