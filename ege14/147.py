x = 49 ** 12 - 7 ** 10 + 7 ** 8 - 49
s = ""
while x > 0:
    s += str(x % 7)
    x = x // 7
print(s.count("6"))
print(s)