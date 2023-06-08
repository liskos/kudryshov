a = []
for i in range(5,10000 + 1,5):
    if (i % 16 == 10) and (i % 7 != 0) and (i % 5 == 0):
        a.append(i)
print(sum(a),len(a))