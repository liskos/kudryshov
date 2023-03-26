x = 7 ** 80 + 49 ** 15 - 49
s = ""
while x > 0:
    s += str(x % 7)
    x = x // 7
print(s.count("6"))
