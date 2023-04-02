

for a in range(1, 999):
    f = all((2 * x + y < a) or (x < y) or (21 <= x) for x in range(0, 1000) for y in range(0, 1000))
    if f:
        print(a)
        break
