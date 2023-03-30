x = 8 ** 4024 - 4 ** 1605 + 2 ** 1024 - 126
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))
