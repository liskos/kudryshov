for x in "0123456789ABCDEFGHIJKLMNOP":
    for y in "0123456789ABCDEFGHIJKLMNOP":
        a1 = "13" + y + x + "5"
        a2 = "24" + y + "13"
        s = int(a1,26) + int(a2,26)
        if s % 8 == 0:
            print(s // 8, x,y)

a1 = "132N5"
a2 = "24213"
s = int(a1,26) + int(a2,26)
print(s//8)


