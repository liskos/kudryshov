x = (2 ** 4400 - 1) * (4 * 2200 + 2)
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
