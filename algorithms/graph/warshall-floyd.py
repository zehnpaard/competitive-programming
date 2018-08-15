from itertools import product

MAX = 2**65

for k, i, j in product(range(n), repeat=3):
    d[i, j] = min(d.get((i, j), MAX), 
                  d.get((i, k), MAX) + d.get((k, j), MAX))
