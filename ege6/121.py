def f(s):
    n = 1
    while s < 51 :
        s = s + 5
        n = n * 2
    return n

for i in range(1,999):
    if f(i) == 64:
        print(i)
        break