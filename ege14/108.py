x = 8 ** 415 - 4 ** 162 + 2 ** 534 - 25
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
