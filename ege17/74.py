def raz(n):
    return len(str(n)) == len(set(str(n)))

def b4(n):
    a = [int(x) for x in str(n) if int(x) > 4]
    return len(a)==3

b = []
for i in range(5903,174203 + 1):
    if raz(i) and b4(i):
        b.append(i)
print(len(b))
c = max([x for x in b if x <= 30000])
print(c)
m = 30000 - min([x for x in b if x >= 30000])
print(m)



