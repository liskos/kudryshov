import sys
sys.stdin = open("24var03.txt")
s = input()

t = ''
m = 99999

for i in s :
    t += i
    x = ""
    while t.count("AB") >= 21:
        x = t[0]
        t = t[1:]
    t = x + t
    if t.count("AB") == 21:
        m = min(m,len(t))
print(m)