def f(a,b):
    return (a+1,b),(a,b+1),(a*3,b),(a,b*3)

a = [["-1"]*800 for _ in range(800)]
for x in range(800):
    for y in range(800):
        if x + y >= 175:
            a[x][y] = "0"

for x in range(800):
    for y in range(800):
        if a[x][y] == "-1" and any(a[i][j] == "0" for i,j in f(x,y)):
            a[x][y] = "1"
for x in range(800):
    for y in range(800):
        if a[x][y] == "-1" and all(a[i][j] == "1" for i,j in f(x,y)):
            a[x][y] = "2"
for x in range(800):
    for y in range(800):
        if a[x][y] == "-1" and any(a[i][j] == "2" for i,j in f(x,y)):
            a[x][y] = "3"
for x in range(800):
    for y in range(800):
        if a[x][y] == "-1" and all(a[i][j] in "13" for i,j in f(x,y)):
            a[x][y] = "4"

for i in range(1,200):
    print(*a[i][1:200],sep = "\t")


