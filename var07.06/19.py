def m(a, b):
    return (a+1,b), (a,b+1),(a*2,b),(a,b*2)


a = [["-1"] * 1000 for x in range(1000)]
for x in range(1000):
    for y in range(1000):
        if x * y >= 455:
            a[x][y] = "0"

for x in range(455):
    for y in range(455):
        if a[x][y] == "-1" and any(a[i][j] == "0" for i,j in m(x,y)):
            a[x][y] = "1"
for x in range(455):
    for y in range(455):
        if a[x][y] == "-1" and all(a[i][j] == "1" for i,j in m(x,y)):
            a[x][y] = "2"
for x in range(455):
    for y in range(455):
        if a[x][y] == "-1" and any(a[i][j] == "2" for i,j in m(x,y)):
            a[x][y] = "3"
for x in range(455):
    for y in range(455):
        if a[x][y] == "-1" and all(a[i][j] in "13" for i,j in m(x,y)):
            a[x][y] = "4"

for i in range(1,500):
    print(*a[i][1:500], sep = "\t")
