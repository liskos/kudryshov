import sys
sys.stdin = open("24var09-13.txt")

s = input()
m = 0
t = ""
k = 0
for i in s:
    if i >=t:
        t = i
        k+=1
    else:
        t = i
        k = 1
    m = max(m,k)
print(m)

