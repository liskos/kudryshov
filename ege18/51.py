import sys
sys.stdin = open("18.k3.txt")

k=0
a = []
for i in range (1000):
    a.append(int(input()))

max = 9999999
for i in range (995):
    if a[i] + a[i+1] < max:
        max = a[i] + a[i+1]
    elif a[i] + a[i+2] < max:
        max = a[i] + a[i+2]
    elif a[i] + a[i + 3] < max:
        max = a[i] + a[i + 3]
    elif a[i] + a[i+4] < max:
        max = a[i] + a[i+4]
    elif a[i] + a[i+5] < max:
        max = a[i] + a[i+5]
print(max)
