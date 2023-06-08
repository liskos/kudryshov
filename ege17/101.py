a = []
for i in range(99,998+1):
    if (i % 10 == 9) and (i % 8 == 1) and (i % 18 != 0):
        a.append(i)

print(len(a),max(a))