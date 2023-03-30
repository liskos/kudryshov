x = 9 ** 17 + 3 ** 16 - 27
s = ""
while x > 0:
    s += str(x % 3)
    x = x // 3
print(s.count("0"),"-0")
print(s.count("1"),"-1")
print(s.count("2"),"-2")
print(s)