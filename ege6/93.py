def f(s):
    n = 0
    while 2*s*s <= 10*s:
        s = s + 1
        n = n + 2
    return n

for i in range(1,999):
    if f(i) == 8:
     print(i)