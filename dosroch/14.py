for x in "0123456789abcdefghijklmnop":
    for y in "0123456789abcdefghijklmnop":
        s1 = "13" + "2" + "n" + "5"
        s2 = "24" + "2"  + "13"
        s  = int(s1,26) + int(s2,26)
        print(s // 8)
