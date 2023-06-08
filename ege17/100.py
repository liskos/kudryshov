a = []
for i in range(100,10000+1):
    if (i % 10 == 3) and (i % 8 == 7) and (i % 21 == 0) and (i % 13 != 0) and (i % 16 != 0) and (i % 19 != 0):
        a.append(i)

print(len(a),max(a))