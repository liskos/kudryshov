def f(n):
    if n > 1000 :
        return '----'
    if n <=  1:
        return n
    if n > 1 and n % 3 == 0:
        if type(f(n // 3)) == str:
            return '-----'
        return n + f(n // 3)
    if n > 1 and n % 3 != 0:
        if type(f(n + 3)) == str:
            return '-----'
        return n + f(n + 3)

for i in range(1,999):
    if type(f(i)) == int and f(i) > 100:
        print(i,f(i))


