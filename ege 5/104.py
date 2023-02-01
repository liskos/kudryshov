for x in range (10,100):
    y1 = (x % 4) * 100
    y2 = (x % 3) * 10
    y3 = (x % 2)
    y = y1 + y2 + y3
    if y == 220:
        print(x,y)
