x = 2 * 27 ** 7 + 3 ** 10 - 9
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("0"))
print(s)