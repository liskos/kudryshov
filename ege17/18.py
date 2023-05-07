a = []
for i in range (980,5320 + 1):
    if ((i % 4 == 0) or (i % 5 == 0)) and (i % 11 != 0) and (i % 17 != 0) and (i % 19 != 0) and (i % 23 != 0):
        a.append(i)
print(len(a),min(a))