def f(n):
    k = ""
    for i in n :
        if i == "0": k += "3"
        elif i == "1" : k += "7"
        elif i == "2":
            k += "2"
        elif i == "3":
            k += "1"
        elif i == "4":
            k += "6"
        elif i == "5":
            k += "0"
        elif i == "6":
            k += "4"
        elif i == "7":
            k += "5"
    return k

b = "32006"
for i in range(13):
    b = f(b)
print(b)


