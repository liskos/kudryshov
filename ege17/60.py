a = []
for i in range(1389,9345 + 1):
    if (i % 2 == 0) and (i % 19 != 0) :
        a.append(i)
print(len(a),sum(a))
print(a)
