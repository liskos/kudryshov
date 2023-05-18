a = []
for i in range(1213,8310 + 1):
    if (i % 3 == 0) and (i % 23 != 0) :
        a.append(i)
print(len(a),sum(a))
print(a)
