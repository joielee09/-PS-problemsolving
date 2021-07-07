import sys
import heapq
import math
sys.setrecursionlimit(10**8)

sys.stdin = open('input.txt')
#도시, 도로, 항공편 갯수 , 시작점, 여행하려는 도시 갯수
n, m, f, s, t = map(int, sys.stdin.readline().split()) 

gph=[[] for _ in range(n+2)]

while m:
  m-=1
  i,j,c = map(int, sys.stdin.readline().split())
  gph[i].append((j,c))
  gph[j].append((i,c))

def dijk(node):
  dist=[ math.inf for _ in range(n+2)]
  edges=[]

  dist[node]=0
  heapq.heappush(edges, (dist[node], node))
  
  while edges:
    cost, pos = heapq.heappop(edges)
    if dist[pos]<cost:
      continue
    for p, c in gph[pos]:
      c+=cost
      if dist[p]>c:
        dist[p]=c
        heapq.heappush(edges, (c,p))
  return dist

ans=math.inf
# airplane
while f:
  f-=1
  u,v = map(int, sys.stdin.readline().split())
  ans = min(dijk(s)[u]+dijk(v)[t], ans)

# by road
ans = min(ans,dijk(s)[t])

print(ans)