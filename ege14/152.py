x = 4 * 125 ** 4 - 25 ** 4 + 9
s = ""
while x > 0:
    s += str(x % 5)
    x = x // 5
print(s.count("4"))
print(s)