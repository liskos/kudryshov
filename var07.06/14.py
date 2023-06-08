for x in "0123456789ABCDE":
    if (int("97968" + x + "13",15) + int("7"+ x + "213",15)) % 11 == 0:
        print(x)