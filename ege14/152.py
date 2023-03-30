x = 4 * 125 ** 4 - 25 ** 4 + 9
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("0"))
print(s)