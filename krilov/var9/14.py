x = 5 ** 2019 - 5 ** 1019 + 25 ** 600 - 125
s = ""
while x > 0:
    s += str(x % 5)
    x = x // 5
print(s.count("4"))
