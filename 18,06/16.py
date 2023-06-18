import sys

sys.setrecursionlimit(10000)

def f(x):
    if x >= 4040:
        return x
    if x < 4040:
        return x + 4 + f(x+4)

print(f(3) - f(15))