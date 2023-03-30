x = 8 ** 125 - 4 ** 156 + 2 ** 623 - 7
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
