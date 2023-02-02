x = 4 ** 2022 - 2 * 4 ** 1111 + 16 ** 600 + 192
s = ""
while x > 0 :
    s += str(x % 4)
    x = x // 4
print(s.count("3"))
    