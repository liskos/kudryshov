def f(a,b):
    s = ""
    while a != 0 :
        s =  str(a%b) + s
        a = a // b
    return int(s)

a = []
for i in range (2807,8558 + 1):
    if ((f(i,2)) % 100 == 11) and ((f(i,9)) % 10 == 5):
        a.append(i)
print(max(a),sum(a))