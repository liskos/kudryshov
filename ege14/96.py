x = 4 ** 2018 + 8 ** 305 - 2 ** 130 - 120
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
