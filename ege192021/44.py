a = [""] * 100
for i in range(0,100):
    if i >= 38:
        a[i] = "0"
for i in range(39):
    if a[i] == "":
        if a[i + 1] == "0" or a[i + 2] == "0" or a[i + 3] == "0" or a[i * 2] == "0":
            a[i] = "1"
for i in range(39):
    if a[i] == "":
        if a[i + 1] == "1" and a[i + 2] == "1" and a[i + 3] == "1" and a[i * 2] == "1":
            a[i] = "2"
for i in range(39):
    if a[i] == "":
        if a[i + 1] == "2" or a[i + 2] == "2" or a[i + 3] == "2" or a[i * 2] == "2":
            a[i] = "3"
for i in range(39):
    if a[i] == "":
        if ((a[i + 1] == "3" or a[i + 1] == "1" )and (a[i + 2] == "3" or a[i + 2] == "1" ) and
                (a[i + 3] == "3" or a[i + 3] == "1" ) and (a[i * 2] == "3" or a[i * 2] == "1")):
            a[i] = "4"

for i in range(100):
    print(i,a[i])

