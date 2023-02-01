for x in range (10,100):
    y1 = (x % 4) * 100
    y2 = (x % 2) * 10
    y3 = (x % 5)
    y = y1 + y2 + y3
    if y == 313:
        print(x,y)
