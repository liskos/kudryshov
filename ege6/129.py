def f(s):
    n = 11
    while s < 224:
        s = s + 15
        n = n + 8
    return n

for i in range(1,999):
    if f(i) == 115:
        print(i)
        break