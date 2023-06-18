for x in "0123456789ABCDEF":
    if (int("1F3B"+x + "75",16) + int("5D"+x + "3B",16)) % 11 == 0:
        print(x,(int("1F3B"+x + "75",16) + int("5D"+x + "3B",16)) // 11)