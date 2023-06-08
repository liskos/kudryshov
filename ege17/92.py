a = []
for i in range(99,999 + 1):
    if (i % 16 == 9) and (i % 9 == 8):
        a.append(i)
print(sum(a),len(a))