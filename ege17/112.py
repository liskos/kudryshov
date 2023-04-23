def f(n):
    m = max(map(int,str(n)))
    s = sum(map(int,str(n)))
    return m == 7 and s == 14 and n % 2 == 0
a=[]
for i in range(1213,2224):
    if f(i) :
        a.append(i)
print(len(a),max(a) - min(a))
