import sys

sys.stdin = open("24var01.txt")

s = input()

t = ""
m = 0
for i in s:
    t += i
    while t.count("A") > 3:
        t = t[1:]
    m = max(m, len(t))
print(m)
