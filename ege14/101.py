x = 8 ** 1341 - 4 ** 1342 + 2 ** 1343 - 1344
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
