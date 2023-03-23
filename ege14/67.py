for x in range(4,999):
    if int("42",5) + x == int("1122",3):
        print(x)

def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]
print(f(22,4))