def f(a,b):
    s = ""
    while a != 0 :
        s =  str(a%b) + s
        a = a // b
    return int(s)

a = []
for i in range (3712,8432 + 1):
    if (((f(i,2)) % 10) == (f(i,4)) % 10) and ((i % 13 == 0) or (i % 14 == 0) or (i % 15 == 0)):
        a.append(i)
print(max(a),sum(a))