x = 2 ** 2014 -4 ** 650 -38
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
