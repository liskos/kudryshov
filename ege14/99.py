x = 8 ** 1234 - 4 ** 234 + 2 ** 1620 - 108
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
