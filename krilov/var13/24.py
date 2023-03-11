import sys
sys.stdin = open("24var09-13.txt")

s = input()
t = ""
m = 0
for i in s:
    t = t + i
    if t.count("Z") <= 2:
        m = max(m,len(t))
    else:
        while t.count("Z") > 2 :
            t = t[1:]
print(m)

