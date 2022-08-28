def f(s):
    n = 1
    while s < 185:
        s = s + 30
        n = n * 3
    return n


for i in range(1,999):
    if f(i) == 729:
        print(i)