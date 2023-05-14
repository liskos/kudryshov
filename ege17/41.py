def f(a,b):
    s = ""
    while a != 0 :
        s =  str(a%b) + s
        a = a // b
    return s

a = []
for i in range (2371,9432 + 1):
    if ((f(i,8))[-2:] == "15" or (f(i,8))[-2:] == "17") and ((i % 3 != 0) and (i % 5 != 0)) :
        a.append(i)
print(len(a),max(a))