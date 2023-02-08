a = set()
for i in range(10,2501):
    n = str(bin(i)[2:])
    n = n.replace("0","")
    a.add(n)
print(len(a))
print(sorted(a))