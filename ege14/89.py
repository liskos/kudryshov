x = 8 ** 1023 + 2 ** 1024 - 3
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
