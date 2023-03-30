x = 4 ** 2015 + 2 ** 2015 - 15
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
