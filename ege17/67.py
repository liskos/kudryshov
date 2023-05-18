b = []
for i in range(100001, 900009 + 1):
    if ((i % 7) + i % 10 == 10) and ((i % 11 == 0) and (i % 55 != 0)):
        b.append(i)

print(max(b),len(b))

def f(n):
    while n >0:
        if n % 10 == 0 or n % 10 == 2:
            return True
    return False


"0" in str(i) or "2" in str(i)