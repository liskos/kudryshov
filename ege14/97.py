x = 8 ** 2018 - 4 ** 305 + 2 ** 124 - 58
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
