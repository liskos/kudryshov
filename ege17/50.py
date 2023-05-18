b= []
def f(a,b):
    s = []
    while a > 0:
        s.append(a % b)
        a = a // b
    return s[::-1]

for i in range(331, 8751 + 1):
    if len(f(i,16)) == len(f(i,10)) and ((i % 5 == 0) and (i % 25 != 0)):
        b.append(i)
print(len(b),min(b))

