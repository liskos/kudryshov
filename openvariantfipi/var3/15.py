for a in range(1, 999):
    f = all((x >=12) or (3 * x < y) or ((x * y) < a) for x in range(0, 1000) for y in range(0, 1000))
    if f:
        print(a)
        break
