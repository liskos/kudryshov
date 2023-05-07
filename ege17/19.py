a = []
for i in range (1305,7850 + 1):
    if ((i % 4 == 0) or (i % 7 == 0)) and (i % 11 != 0) and (i % 17 != 0) and (i % 19 != 0) and (i % 21 != 0):
        a.append(i)
print(len(a),min(a))