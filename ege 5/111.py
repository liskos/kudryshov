s = "115"
for f1 in (1,2,4,5,6,9):
    for f2 in (1,2,4,5,6,9):
        for f3 in (1, 2, 4, 5, 6, 9):
            for f4 in (1, 2, 4, 5, 6, 9):
                f = str(f1 + f3) + str(f2 + f4)
                if f == s:
                    print(f1,f2,f3,f4,s )
