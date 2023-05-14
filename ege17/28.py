def f(a,b):
    s = ""
    while a != 0 :
        s =  str(a%b) + s
        a = a // b
    return int(s)

a = []
for i in range (3439,7410 + 1):
    if (((f(i,2)) % 10) != (f(i,6)) % 10) and ((i % 9 == 0) or (i % 10 == 0) or (i % 11 == 0)):
        a.append(i)
print(len(a),max(a))