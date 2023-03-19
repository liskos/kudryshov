import sys
sys.stdin = open("24var14-20.txt")

s = input()
m = 0
t = ''
k = 0
for i in s:
    if i > t:
        k += 1
        m = max(m,k)
    else:
        k = 1
    t = i
print(m)
