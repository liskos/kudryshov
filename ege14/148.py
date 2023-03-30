x = 27 ** 4 - 9 ** 5 + 3 ** 8 - 25
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("2"))
print(s)