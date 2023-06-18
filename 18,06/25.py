def f(n):
    a = set()
    for i in range(1,int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    b = [i for i in a if len(str(i)) == 4 and str(i)[-1] == "0"]
    return len(b), b

for i in range(5 * 10 ** 5,10**6,10):
    x, y = f(i)
    if x > 45:
        print(i, x)
