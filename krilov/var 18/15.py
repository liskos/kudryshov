def func(a):
    for x in range(0,999):
        for y in range(0,999):
            f = (x + y <= 32) or (y <= x + 4) or (y >= a)
            if not f:
                return False
    return True


for a in range(1,99999):
    if func(a):
        print(a)
