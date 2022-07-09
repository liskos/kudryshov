def f(s):
    for k in range(3,9):
        s = s + k
    return s


for i in range(1, 999):
    if f(i) > 100:
        print(i)
        break