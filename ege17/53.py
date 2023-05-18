a = []
for i in range(10,1178 + 1):
    if (i % 2 == 0) and (i % 10 != 0) and (i % 10 != 2) and (i % 10 != 6) and (i % 10 != 8) and (i % 10 != 14):
        a.append(i)
print(sum(a),min(a))
print(a)
