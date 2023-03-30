x = 4 * 25 ** 4 - 5 ** 4 + 14
s = ""
while x > 0:
    s += str(x % 5)
    x = x // 5

print(s)
