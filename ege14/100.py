x = 8 ** 2341 - 4 ** 342 + 2 ** 620 - 81
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
