def f(n,m):
    if n<m:
        n,m = m,n
    if n != m :
        return f(n-m,m)
    else :
        return n

s = 200
im = 200
ig = 200
for i in range(1,100):
    for g in range(1,100):
        if f(i,g) > 15 and i != g :
            if i + g < s:
                s = i + g
                im = i
                ig = g
print(im,ig, f(im,ig))
