def f(a,b):
    s = ""
    while a != 0 :
        s =  str(a%b) + s
        a = a // b
    return s

a = []
for i in range (1529,9482 + 1):
    if f(i,2)[-2:] == "01" and f(i,5)[-1:] == "3":
        a.append(i)
print(min(a),sum(a))