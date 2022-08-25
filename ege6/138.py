def f(s):
    n = 600
    while n > s:
        s = s + 3
        n = n - 6
    return n


for i in range(-991,999):
    if f(i) == 210:
        print(i)