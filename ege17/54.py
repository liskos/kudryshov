a = []
for i in range(2595,8401 + 1):
    if (i % 2 == 0) and (i % 13 != 0) :
        a.append(i)
print(len(a),sum(a))
print(a)
