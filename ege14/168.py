x = 9 ** 14 + 3 ** 18 - 9 ** 5 - 27
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("2"))
print(s)