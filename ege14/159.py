x = 9 ** 20 + 3 ** 60 - 15
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("2"))
print(s)