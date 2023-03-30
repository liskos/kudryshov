x = 8 ** 115 - 4 ** 123 + 2 ** 543 - 15
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
