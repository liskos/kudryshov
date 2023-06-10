def f(a):
    if all(not(x % 2 == 0) or (x % 3 !=0) or (x + a >=100) for x in range(1,1000)):
        return True
    return False

for i in range(1,1000):
    if f(i):
        print(i)
