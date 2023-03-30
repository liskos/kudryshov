x = 4 ** 1024 + 8 ** 1025 - 2 ** 1026 - 140
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
s = s[::-1]
print(s.count("0"))
print(s)
