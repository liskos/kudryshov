x = 5 ** 28 + 25 ** 6 - 125
s = ""
while x > 0:
    s += str(x % 5)
    x = x // 5
print(s.count("4"))
print(s)
