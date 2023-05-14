a = []
for i in range (3712,8432 + 1):
    if (i % 2 == i % 4) and ((i % 13 == 0) or (i % 14 == 0) or (i % 15 == 0)):
        a.append(i)
print(len(a),min(a))