import sys
sys.stdin = open("24var09-13.txt")

s = input()

s = s.replace("YX","Y X")
s = s.replace("ZY","Z Y")
s = s.replace("ZX", "Z X")
print (max(map(len,s.split())))