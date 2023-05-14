for x in "0123456789ABCDE":
    a1 = "97968" + x + "15"
    a2 = "7" + x + "233"
    s = int(a1,15) + int(a2,15)
    if s % 14 == 0:
        print(s // 14)

