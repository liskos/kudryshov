a = [[""] * 200 for _ in range(200)]
for i in range(120):
    for j in range(120):
        if i + j >= 57:
            a[i][j] = "0"
for i in range(120):
    for j in range(120):
        if a[i][j] == "" and (a[i+1][j] == "0" or a[i][j+1] == "0" or a[i*2][j] == "0" or a[i][j*2] == "0") :
            a[i][j] = "1"
for i in range(120):
    for j in range(120):
        if a[i][j] == "" and (a[i+1][j] == "1" and a[i][j+1] == "1" and a[i*2][j] == "1" and a[i][j*2] == "1") :
            a[i][j] = "2"
for i in range(120):
    for j in range(120):
        if a[i][j] == "" and (a[i+1][j] == "2" or a[i][j+1] == "2" or a[i*2][j] == "2" or a[i][j*2] == "2") :
            a[i][j] = "3"
for i in range(120):
    for j in range(120):
        if a[i][j] == "" and ((a[i+1][j] == "1" or a[i+1][j] == "3")  and (a[i][j+1] == "1" or a[i][j+1] == "3")
                              and (a[i*2][j] == "1" or a[i*2][j] == "3") and (a[i][j*2] == "1" or a[i][j*2] == "3")) :
            a[i][j] = "4"



for i in range(1,120):
     print(*a[i][1::], sep="\t")
