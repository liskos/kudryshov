x = 2 ** 1024 + 2 ** 1026
s = ""
while x > 0:
    s += str(x % 8)
    x = x // 8
s = s[::-1]
print(len(s))
print(s)
