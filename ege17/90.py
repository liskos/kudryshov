a = []
for i in range(12094,20075 + 1):
    if (i % 16 == 15) and (i % 3 == 0) and (i % 8 != 0) and (i % 14 != 0) and (i % 19 != 0):
        a.append(i)
print(sum(a),len(a))