x = 2 ** 1024 + 2 ** 1025
s = ""
while x > 0:
    s += str(x % 16)
    x = x // 16
s = s[::-1]
print(len(s))
print(s)
