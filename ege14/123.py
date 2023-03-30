x = 8 ** 2020 +4**2017+2**6-1
s = ""
while x > 0:
    s += str(x % 2)
    x = x // 2
print(s.count("1"))

