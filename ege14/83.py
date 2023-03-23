for x in range(1,999):
    if int("100",5) + x == int("200",4):
        print(x)

def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]
print(f(7,7))