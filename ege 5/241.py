a = []
for i in range(1,256):
    n = bin(i)[2:]
    if len(n) < 8:
        n = "0" * (8-len(n)) + str(n)
    b = n[::-1]
    s = int(n,2) - int(b,2)
    a.append(s)

print(max(a))