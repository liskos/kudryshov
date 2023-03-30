x = 8 ** 820 - 2 ** 760 + 14
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))

