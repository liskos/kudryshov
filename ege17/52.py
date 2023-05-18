b= []
def f(a,b):
    s = []
    while a > 0:
        s.append(a % b)
        a = a // b
    return s[::-1]

for i in range(1000, 70000 + 1):
    if (len(f(i,8)) == 5 and len(f(i,5)) == 6) and (i % 16 == 10) and (i // 16 % 16 == 14)  :
        b.append(i)
print(len(b),max(b))

