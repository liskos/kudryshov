a = []
for i in range (3672,9117 + 1):
    if (i % 3 == 2) and (i % 5 == 4):
        a.append(i)
print(max(a),sum(a))