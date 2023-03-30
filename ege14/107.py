x = 8 ** 502 - 4 ** 211 + 2 ** 1536 - 19
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
