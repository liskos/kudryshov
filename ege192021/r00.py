import functools

functools.lru_cache()
def h(x, y):
    return (x+1, y), (x, y+1), (x*2, y), (x,y*2)

functools.lru_cache()
def reh(x, y):
    if x + y >= 77:
        return 0
    if any(i + j >= 77 for i, j in h(x, y)):
        return 1
    if all(reh(i, j) == 1 for i, j in h(x, y)):
        return 2
    if any((reh(i, j) == 2 or reh(i, j) == 0) for i, j in h(x,y)):
        return 3
    if all(reh(i,j) == 3 or reh(i,j) == 1 for i,j in h(x,y)):
        return 4


for s in range(69, 1, -1):
    print(s, reh(7, s))