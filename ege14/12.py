def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]


s = 0
for a in range(12,32):
    s += f(a,5).count(1)
print(s)