x = 8 ** 1014 - 2 ** 530 - 12
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
