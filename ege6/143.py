def f(x):
    k = 0
    while x < 100:
        if x % 2 < 1:
            x = x // 2
        else :
            x = 3 * x + 1
        k += 1
        if k == 100000:
            return "------"
    return x

for i in range(1,999):
       print(i, f(i))