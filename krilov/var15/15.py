def func(a):
    for x in range(1,999):
        for y in range(1,999):
            f = (x < a) and (y < a) and ((x * y) > 601)
            if f:
                return False
    return True


for a in range(1,99999):
    if func(a):
        print(a)