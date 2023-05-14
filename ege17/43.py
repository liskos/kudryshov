def f(a,b):
    s = ""
    while a != 0 :
        s = str(a % b) + s
        a = a // b
    return s

a = []
for i in range (9721,7752 + 1):
    if sum(map(int, s)) == 3 and f(i,2)[-3:] != "000" :
        a.append(i)
print(len(a),min  (a))