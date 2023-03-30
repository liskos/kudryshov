x = 9 ** 7 + 3 ** 21 - 8
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("2"))
print(s)