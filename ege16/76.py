def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0 :
        if type(f(n // 2 - 1)) == str:
            return '--------'
        return 3 + f(n // 2 - 1)
    if n > 1 and n % 2 != 0:
        return '-----'

for i in range(1,998):
    print(i,f(i))
    if f(i) == 19:
        print(i)
        break