def f(s):
    for i in range(len(s)-3):
        if s[i]=="Q" and s[i+3]=="A":
            return True
    return False


import sys
sys.stdin = open("24.txt")
k = 0
for i in range(1000):
    if f(input()):
        k += 1
print(k)
