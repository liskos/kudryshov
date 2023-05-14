def f(a,b):
    s = ""
    while a != 0 :
        s =  str(a%b) + s
        a = a // b
    return s

a = []
for i in range (1871,9197 + 1):
    if len(f(i,16)) != len(f(i,10)) and (i % 9 == 2 or i % 9 == 4 ):
        a.append(i)
print(len(a),min(a))