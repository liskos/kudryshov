i = 27
a = []
while i <= 900000:
    if len(set(str(i))) == len(str(i)):
        a.append(i)
    i = i * 2
print(len(a),max(a))
print(a)