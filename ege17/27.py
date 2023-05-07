a = []
for i in range (3712,8432 + 1):
    if (i % 3 == 2) and (i % 5 == 4):
        a.append(i)
print(max(a),sum(a))