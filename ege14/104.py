for x in range(6, 37):
    if int("145", x) + 24 == int("127", 9):
        print(x)

def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]
print(f(7,5))