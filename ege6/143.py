def f(x):
    while x < 100:
        if x % 2 < 1:
            x = x // 2
        else :
            x = 3 * x + 1
    return x

for i in range(1,999):
    if f(i) > 0:
       print(i)