x = 4 ** 2016 + 2 ** 2018 - 6
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
