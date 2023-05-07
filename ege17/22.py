a = []
for i in range (2477,7849 + 1):
    if (i % 2 == 0) and (i % 5 != 0) and (i % 8 != 0) and (i % 9 != 0) and (i % 13 != 0):
        a.append(i)
print(len(a),min(a))