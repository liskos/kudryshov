for a in range(1, 999):
    f = all(not(y + 2*x <= 27) or ((y - x > 3) or (y <= a)) for x in range(0, 1000) for y in range(0, 1000))
    if f:
        print(a)
        break
