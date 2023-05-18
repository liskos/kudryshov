b= []
def f(a,b):
    s = []
    while a > 0:
        s.append(a % b)
        a = a // b
    return s[::-1]

for i in range(117649, 823542 + 1):
    if len(f(i,7)) == 7 and (i % 3 == 2) and (i % 8 != 3) and (i % 12 != 5) :
        b.append(i)
print(len(b),max(b))

