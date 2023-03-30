def func(a):
    for x in range(0,999):
        for y in range(0,999):
            f = (3 * x + y < a ) or (x < y) or (16 <= x)
            if not f:
                return False
    return True


for a in range(1,99999):
    if func(a):
        print(a)