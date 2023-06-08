a = []
for i in range(9999,99999 + 1):
    if i % sum(map(int,str(i))) == 0:
        a.append(i)
print(len(a),max(a))
        