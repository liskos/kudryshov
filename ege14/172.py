x = 9 ** 9 + 3 ** 21 - 7
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("0"))
print(s)