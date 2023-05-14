def f(a,b):
    s = ""
    while a != 0 :
        s = str(a % b) + s
        a = a // b
    return s

a = []
for i in range (2495,7083 + 1):
    if ((f(i,16))[-2:] == "1A" or (f(i,16))[-2:] == "1F") and ((i % 5 != 0) and (i % 9 != 0)) :
        a.append(i)
print(len(a),min(a))