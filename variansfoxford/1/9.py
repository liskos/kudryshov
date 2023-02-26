import sys
sys.stdin = open("9.txt")

def f(a):
    for i in range(6):
        if a.count(a[i]) == 3:
            b = set(a)
            if len(b) == 4 and (sum(b) - a[i]) / 3 >= 3 * a[i]:
                return True
    return False



k = 0
for i in range(6400):
    a = list(map(int,input().split()))
    if f(a):
        k += 1
print(k)


