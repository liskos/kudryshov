a = set()
for f1 in (1,2,3,4,5,6,7,8,9):
    for f2 in (1,2,3,4,5,6,7,8,9):
        for f3 in (1,2,3,4,5,6,7,8,9):
            for f4 in (1,2,3,4,5,6,7,8,9):
                s12 = f1 + f2
                s23 = f2 + f3
                s34 = f3 + f4
                m = min(s12,s23,s34)
                a.add(s12)
                a.add(s23)
                a.add(s34)
                sorted(a)
if



