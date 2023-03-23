for x in range(1,999):
    if int("60",8) + x == int("200",5):
        print(x)

def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]
print(f(2,6))