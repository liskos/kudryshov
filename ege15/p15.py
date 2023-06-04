def f(a):
    p = {i for i in range(50, 301)}
    q = {i for i in range(140, 231)}
    for x in  {i for i in range(0, 500)}:
        c = not ((x in p) == (x in q)) or ( x not in a)
        if not c:
            return False
    return True


for j in {i for i in range(0, 500)}:
    if f({j}):
        print(j/10, end=" ")


