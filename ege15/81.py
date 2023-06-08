def f(a):
    p = {i for i in range(2, 42+1)}
    q = {i for i in range(22, 62+1)}
    for x in  {i for i in range(0, 500)}:
        c = not(not(x in p) or (x not in q)) or (x not in a)
        if not c:
            return False
    return True


for j in {i for i in range(0, 500)}:
    if f({j}):
        print(j, end=" ")


