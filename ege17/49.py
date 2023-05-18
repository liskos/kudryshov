b= []
def f(a,b):
    s = []
    while a > 0:
        s.append(a % b)
        a = a // b
    return s[::-1]

for i in range(127, 9852 + 1):
    if len(f(i,8)) == len(f(i,10)) and ((i % 3 == 0) and (i % 9 != 0)):
        b.append(i)
print(len(b),max(b))

