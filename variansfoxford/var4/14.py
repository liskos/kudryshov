for x in "0123456789ABCDEFGH":
    a1 = "1" + x + "239"
    a2 = "2" + x + "C" + x
    s = int(a1,18) + int(a2,18)
    if s % 19 == 0:
        print(s // 19)

