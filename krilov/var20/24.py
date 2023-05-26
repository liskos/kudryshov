import sys
sys.stdin = open("24var14-20.txt")

s = input()
s = s.replace("0"," 0 ")
s = s.replace("2"," 2 ")
s = s.replace("4"," 4 ")
s = s.replace("6"," 6 ")
s = s.replace("8"," 8 ")
print(max(map(len,s.split())))