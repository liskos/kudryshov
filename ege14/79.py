for x in range(1,999):
    if int("14",5) + x == int("24",7):
        print(x)

def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]
print(f(9,3))