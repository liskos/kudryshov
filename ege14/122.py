x = 8 ** 560 - 2 ** 234 + 56
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
s = s[::-1]
print(s.count("0"))
print(s)
