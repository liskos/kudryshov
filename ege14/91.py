x = 4 ** 2014 + 2 ** 2015 - 9
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
