import sys
sys.stdin = open("1_24.txt")

a = input()

a = a.replace("AA","A A")
a = a.replace("BB","B B")
a = a.replace("CC","C C")
a = a.replace("AB","A B")
a = a.replace("AC","A C")
a = a.replace("BA","B A")
a = a.replace("BC","B C")
a = a.replace("CA","C A")
a = a.replace("CB","C B")


print(max(map(len,a.split())))
print(a)


