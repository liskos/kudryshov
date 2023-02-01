for x in range (10,100):
    y1 = (x % 2) * 100
    y2 = (x % 3) * 10
    y3 = (x % 5)
    y = y1 + y2 + y3
    if y == 122:
        print(x,y)
