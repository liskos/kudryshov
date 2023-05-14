def f(a,b):
    s = ""
    while a != 0 :
        s =  str(a%b) + s
        a = a // b
    return s

a = []
for i in range (3466,9081 + 1):
    if len(f(i,8)) != len(f(i,10)) and (i % 7 == 1 or i % 7 == 5 ):
        a.append(i)
print(len(a),max(a))