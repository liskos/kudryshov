for i in range (1007,746001 + 1):
def p(n):
    s1 = str(n)[0]
    s = str(n)[1:]
    for i in s:
        if s1 < i:
            return False
    return True

a = []
b = []
for i in range(1007,746001 + 1):
    if p(i) and (str(i).count("5") % 2 == 0 and str(i).count("5") >= 2):
        a.append(i)
        if str(i)[:2] == "50":
            b.append(i)
print(a)
print(len(a))
print(max(b))
