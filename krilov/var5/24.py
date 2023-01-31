import sys
sys.stdin = open("24var05-08.txt")

x = list(map(len,input().split("00")))
print(x)
print(max(x)+2)

