a = set()
b = set()
c = set()
def f(s):
    for s1 in "АБВГД":
        for s2 in "АБВГД":
            for s3 in "АБВГД":
                s = s1 + s2 + s3
                a.add(s)
                return a


def d(s):
    for s1 in "АБВГДЯ":
        for s2 in "АБВГД":
            for s3 in "АБВГД":
                s = s1 + s2 + s3
                b.add(s)
                return b

def g(s):
    for s1 in "АБВГД":
        for s2 in "АБВГД":
            for s3 in "АБВГДЯ":
                s = s1 + s2 + s3
                c.add(s)
                return c
print(len(a) + len(b) + len(c))
print(a)