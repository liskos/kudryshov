def f(a):
    for x in range(1,100+1):
        c = (x % a == 0) or ((x % 6 != 0) or (x % 4 !=0))
        if not c:
            return False
    return True

for a in range(1,100):
    if f(a):
        print(a)


