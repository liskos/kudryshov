for x in "0123456789ABCDEFG":
    a1 = "1C3" + x + "6"
    a2 = "1" + x + "4" + x
    s = int(a1,17) + int(a2,17)
    if s % 18 == 0:
        print(s // 18)
        break
