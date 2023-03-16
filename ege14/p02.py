x = int("1700000",8) +  int("170000",8) + int("17000",8) + int("1700",8) + int("170",8) + int("17",8)
s = []
while x != 0 :
    s.append(x % 16)
    x = x // 16
print(s[::-1])
    