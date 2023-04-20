a = [[""] * 50 for _ in range(50)]
for x in range(33):
    for y in range(33):
        if x + y <= 32:
            a[x][y] = "0"
for x in range(50):
    for y in range(50):
        if a[x][y] == "":
            if a[x - 1][y] == "0" or  a[x][y-1] == "0" or a[x // 2 + x % 2][y] == "0" or a[x][y // 2 + y % 2] == "0":
                a[x][y] = "1"
for x in range(50):
    for y in range(50):
        if a[x][y] == "":
            if a[x - 1][y] == "1" and  a[x][y-1] == "1" and a[x // 2 + x % 2][y] == "1" and a[x][y // 2 + y % 2] == "1":
                a[x][y] = "2"
for x in range(50):
    for y in range(50):
        if a[x][y] == "":
            if a[x - 1][y] == "2" or  a[x][y-1] == "2" or a[x // 2 + x % 2][y] == "2" or a[x][y // 2 + y % 2] == "2":
                a[x][y] = "3"
for x in range(50):
    for y in range(50):
        if a[x][y] == "":
            if ((a[x - 1][y] == "1" or a[x - 1][y] == "3")  and (a[x][y-1] == "1" or a[x][y-1] == "3" ) and
                    (a[x // 2 + x % 2][y] == "1" or a[x // 2 + x % 2][y] == "3" )  and (a[x][y // 2 + y % 2] == "1" or a[x][y // 2 + y % 2] == "3" )):
                a[x][y] = "4"






for i in range(1,50):
    print(*a[i][1:],sep="\t")
