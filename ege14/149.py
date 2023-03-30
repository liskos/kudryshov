x = 3 * 16 ** 8 - 4 ** 5 + 3
s = ""
while x > 0:
    s += str(x % 4)
    x = x // 4
print(s.count("3"))
print(s)