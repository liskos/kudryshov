b = []
m = 0
def f(n):
    if n == 1:
        return True
    if n % 3 == 0:
        return f(n//3)
    return False


for i in range(138, 603884 + 1):
    a = i
    if len(set(str(i))) < len(str(i)) and f(i):
        b.append(i)
        if (sum(map(int,str(a)))) > (sum(map(int,str(m)))):
            m = a
print(len(b),m)
