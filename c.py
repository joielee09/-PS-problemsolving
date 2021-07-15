k = 20
n = 10000
m = 4
x = (n-k*2-2-m) // 2
y = (n-k*2-2-m) - x
edges = []
def e(u, v, w): edges.append((u+1, v+1, w))
for i in range(k): e(i, i+1, 10000); e(n-k+i-1, n-k+i, 10**6)
for t in range(k+1, k+x+1):
    e(k, t, t-k)
    for j in range(m): e(t, k+x+1+j, 10000 - 2*(t-k))
for t in range(k+x+1+m, k+x+1+m+y):
    for j in range(m): e(k+x+1+j, t, 1)
    e(t, n-k-1, 10**6)

print(n, len(edges), k); assert 1 <= len(edges) <= 50000
for u, v, w in edges:
    assert 1 <= u <= n >= v >= 1 <= w <= 10**6
    print(u, v, w)