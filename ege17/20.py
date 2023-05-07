a = []
for i in range (1045,8963 + 1):
    if ((i % 5 == 0) or (i % 7 == 0)) and (i % 11 != 0) and (i % 13 != 0) and (i % 17 != 0) and (i % 19 != 0):
        a.append(i)
print(len(a),min(a))