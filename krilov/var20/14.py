x = 3 ** 2017 + 9 ** 1000 + 9 ** 100 - 81
a = []
while x > 0:
    a.append(x % 3)
    x = x // 3
print(a.count(2))
print(a)