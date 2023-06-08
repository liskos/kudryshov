a = []
for i in range(100,1000 + 1):
    if (i % 16 == 0) and (i % 3 != 0):
        a.append(i)
print(sum(a),len(a))