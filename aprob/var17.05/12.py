import sre_compile

def f(n):
    s = "2" + n * "5"
    while ("25" in s) or ("355" in s) or ("555" in s):
        if "25" in s:
            s = s.replace("25","5",1)
        if "355" in s:
            s = s.replace("355","52",1)
        if "555" in s:
            s = s.replace("555","3",1)
    return s

for i in range(4,999):
    if f(i).count("3") == 2:
        print(i,f(i))
        break