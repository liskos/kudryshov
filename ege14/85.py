for x in range(1,999):
    if int("100",7) + x == int("214",5):
        print(x)

def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]
print(f(10,6))