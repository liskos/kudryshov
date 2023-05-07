a = []
for i in range (1221,9763 + 1):
    if (i % 7 == 0) and (i % 2 != 0) and (i % 5 != 0) and (i % 11 != 0) and (i % 49 != 0):
        a.append(i)
print(len(a),max(a))