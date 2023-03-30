x = 8 ** 148 - 4 ** 123 + 2 ** 654 - 17
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
