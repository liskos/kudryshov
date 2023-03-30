import sys
sys.stdin = open("24var04.txt")
s = input()

t = ''
m = 0

for i in s :
    t += i
    while t.count("AB") > 21:
        t = t[1:]
    if t.count("AB") == 21:
        m = max(m,len(t))
print(m)