x = 2 ** 299 + 2 ** 298 + 2 ** 297 + 2 ** 296
s = ""
while x > 0:
    s += str(x % 8)
    x = x // 8
s = s[::-1]
print(len(s))
print(s)
