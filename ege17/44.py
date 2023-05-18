def f(a,b):
    s = ""
    while a != 0 :
        s = str(a % b) + s
        a = a // b
    return s


a = []
for i in range (3912,9193 + 1):
    if sum(map(int, f(i,10))) % 9 == 0 and (not(i%16 == 1 and i//16%16 == 2 )) :
        a.append(i)
print(len(a),min(a))