def f(m, k):
    p = {i for i in range(2, 42+1)}
    q = {i for i in range(22, 62+1)}
    a = {i for i in range(m, k+1)}
    for x in range(0, 500):
        c = not(not(x in p) or (x not in q)) or (x not in a)
        if not c:
            return False
    return True


print(f(3, 14))
print(f(23, 32))
print(f(43, 54))
print(f(15, 45))