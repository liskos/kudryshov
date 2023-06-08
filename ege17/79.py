def prost(n):
    a = []
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    if len(a) == 2:
        return True
    return False

b = []
c = []
for i in range(2095,19402+1):
    if prost(i) and str(i)[0] > str(i)[-1]:
        b.append(i)
    if i % 100 == 21:
        c.append(i)


print(len(b))
print(max(c))


