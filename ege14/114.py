x = 4 ** 590 + 8 ** 350 - 2 ** 1020 - 25
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
s = s[::-1]
print(s.count("0"))
print(s)
