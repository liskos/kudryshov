x = 9 ** 8 + 3 ** 24 - 18
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("2"))
print(s)