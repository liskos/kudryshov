def func(a):
    for x in range(1,400):
        for y in range(1,400):
            f = (x >= a) or (y >= a) or (x * y <= 200)
            if not f:
                return False
    return True


for a in range(1,99999):
    if func(a):
        print(a)