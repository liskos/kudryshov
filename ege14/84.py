for x in range(1,999):
    if int("60",8) + x == int("60",9):
        print(x)

def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]
print(f(6,6))