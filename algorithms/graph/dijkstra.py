from heapq import heappop, heappush

MAX = 2**65

d = {0:0}
q = [(0, 0)]

while q:
    du, u = heappop(q)
    if du > d[u]: continue
    for v, w in e[u]:
        if du + w >= d.get(v, MAX): continue
        d[v] = du + w
        heappush(q, (d[v], v))
