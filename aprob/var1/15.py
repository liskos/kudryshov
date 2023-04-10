for a in range(1, 999):
    f = all((x + y <= 32) or (y <= x + 4) or (y >= a) for x in range(0, 1000) for y in range(0, 1000))
    if f:
        print(a)
        break
