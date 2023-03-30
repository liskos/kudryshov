x = 2 ** 379 + 2 ** 378 + 2 ** 377
s = []
while x > 0:
    s.append(x % 16)
    x = x // 16
s = s[::-1]
print(len(s))
print(s)
