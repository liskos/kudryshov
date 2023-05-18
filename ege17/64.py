a = []
for i in range(4563,7912 + 1):
    if (i % 7 == 0) and ((i % 10 + i // 1000 % 10) > 10) :
        a.append(i)
print(max(a),len(a))

