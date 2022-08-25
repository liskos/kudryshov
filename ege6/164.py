def f(x):
    n = 1531
    while (x + n) // 1000 < 253729:
        x = x - 3
        n = n + 7
    return n // 1000

for i in range(1,999):
    if f(i) == 526:
        print(i)