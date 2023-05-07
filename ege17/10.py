a = []
for i in range (1098,13765 + 1):
    if (i % 2 == 0) and (i % 7 != 0) and (i % 11 != 0) and (i % 13 != 0) and (i % 23 != 0):
        a.append(i)
print(len(a),min(a))