import sys
import heapq
import math

sys.stdin=open("input.txt")

v,e = map(int, sys.stdin.readline().split())

dist=[math.inf for i in range(v+2)]
gph=[[] for i in range(v+2)]
edges=[]

while e:
  e-=1
  a,b,c = map(int, sys.stdin.readline().split())
  gph[a].append((b,c))
  gph[b].append((a,c))

v1,v2 = map(int,sys.stdin.readline().split())
answer=0

def dijk(start, end):
  dist=[math.inf for i in range(v+2)]
  edges=[]
  dist[start]=0
  heapq.heappush(edges,(dist[start],start))
  while edges:
    cost, pos = heapq.heappop(edges)
    for p,c in gph[pos]:
      c+=cost
      if dist[p]>c:
        dist[p]=c
        heapq.heappush(edges,(c,p))
  return dist[end]

check = max(dijk(1,v1)+dijk(v1,v2)+dijk(v2,v), dijk(1,v2)+dijk(v2,v1)+dijk(v2,v))
answer = min(dijk(1,v1)+dijk(v1,v2)+dijk(v2,v), dijk(1,v2)+dijk(v2,v1)+dijk(v1,v))

print(dijk(1,v1)+dijk(v1,v2)+dijk(v2,v))
print(dijk(1,v2)+dijk(v2,v1)+dijk(v1,v))

if check==math.inf:
  print(-1)
else:
  print(answer)