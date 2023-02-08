a = set()
for i in range(20,601):
    n = int(str(bin(i))[2:-2],2)
    a.add(n)

print(len(a))