def f(s):
    n = 8
    while n < 510:
        s = s + (n //2)
        n = 2 + n
    return s - n

for i in range(1,999):
    if f(i) == 32299:
        print(i)