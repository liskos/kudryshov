for x in "0123456789ABCDEFGHIJK":
    for y in "0123456789ABCDEFGHIJK":
        a1 = "12" + y + x + "9"
        a2 = "36" + y + "99"
        s = int(a1,21) + int(a2,21)
        if s % 18 == 0:
            print(s // 18, x,y)
            break

a1 = "12539"
a2 = "36599"
s = int(a1,21) + int(a2,21)
print(s//18)