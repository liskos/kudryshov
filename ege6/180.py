def f(s):
    n = 50
    k = 0
    while n > 0:
        n = s // n
        s = s // 2
        k += 1
        if k == 100000:
            return "------"
    return s

print(f(41000000))
print(f(40900000))