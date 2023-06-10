from fnmatch import *
for x in range(4013,10**9,4013):
    if fnmatch(str(x),"123?4*5679"):
        print(x,x//4013)