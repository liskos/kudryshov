from itertools import *
k = 0
for i in product("АВЛОР",repeat = 4):
    k += 1
    if "Л" == i[0]:
        print(k,i)
