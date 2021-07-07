import sys
import heapq
import math

sys.stdin=open("input.txt")

v,e = map(int, sys.stdin.readline().split())
s = int(sys.stdin.readline())

dist = [math.inf for i in range(v+2)]
gph = [[] for i in range(v+2)]
edges=[]

while e:
  e-=1
  u,v,w = map(int, sys.stdin.readline().split())
  gph[u].append((v,w))

dist[s]=0
heapq.heappush(edges,(dist[s],s))
while edges:
  cost, pos = heapq.heappop(edges)
  for p, c in gph[pos]:
    c+=cost
    if dist[p]>c:
      dist[p]=c # 업데이트
      heapq.heappush(edges,(c,p))

for item in dist[1:-1]:
  if item==math.inf:
    print("INF")
  else:
    print(item)