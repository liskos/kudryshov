a = []
for i in range(2738,7514 + 1):
    if (i % 7 == 0) and (i % 19 != 0) :
        a.append(i)
print(len(a),sum(a))
print(a)
