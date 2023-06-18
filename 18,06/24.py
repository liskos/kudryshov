import sys

sys.stdin = open("24 (1).txt")

def f(s):
    if len(s) < 5 :
        return True
    for i in range(len(s)-4):
        if s[i+1] == "B" and s[i + 4] == "D":
            return False
    return True


s = input()

m = 0
t = ""
for i in s:
    t += i
    while f(t) and len(t)>=5:
        t = t[1:]
    m = max(m,len(t))

print(m)
