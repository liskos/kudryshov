x = 4 ** 2015 + 8 ** 2016 - 2 ** 2017 - 150
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
s = s[::-1]
print(s.count("0"))
print(s)
