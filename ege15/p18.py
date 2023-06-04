def f(n):
    s = ""
    for i in range(8):
        s += str(n % 2)
        n = n // 2
    return s[::-1]

def g(a):
    p = {i for i in a if i[0] == "1"}
    q = {i for i in a if i[-3:] == "000"}
    for x in {f(i) for i in range(0,256)}:
        h = (x in a) or ((x not in p) or (x in q))
        if not h:
            return False
    return True


a = {f(i) for i in range(0,256)}


for i in {f(i) for i in range(0,256)}:
    a.remove(i)
    if not g(a):
        a.add(i)
print(len(a))




