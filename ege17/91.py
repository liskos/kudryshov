a = []
for i in range(697,3458 + 1):
    if (i % 16 == 14) and (i % 8) == (i % 7):
        a.append(i)
print(sum(a),len(a))