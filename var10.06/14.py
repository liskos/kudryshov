a = []
for x in "0123456789ABCDEF":
    for y in "0123456789ABCDEF":
        if (int("27A" + x + "23",16) + int("8" + y + "E5D2",16)) % 5 == 0:
            a.append(int(x,16) + int(y,16))
print(max(a))