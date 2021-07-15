import sys
import heapq
import math
from collections import deque

sys.stdin=open('input.txt')

N, M, K = map(int, sys.stdin.readline().split())
gph=[[] for _ in range(N+2)]
while M:
  M-=1
  a,b,c = map(int, sys.stdin.readline().split())
  gph[a].append((b,c))
  gph[b].append((a,c))

# node에서 N까지 K를 사용하는 다익스트라
def dijk(node):
  dist=[[math.inf for _ in range(K+2)] for __ in range(N+2)]
  edges=[]
  cnt=0
  dist[node][cnt]=0 #start:1 , end node: 1, cnt: 0
  # pq: cost, pos, cnt
  heapq.heappush(edges,(dist[node][0], 1, cnt))

  while edges:
    cost, pos, cnt = heapq.heappop(edges)
    if dist[pos][cnt]<cost:
      continue
    for p,c in gph[pos]:
      c+=cost
      if dist[p][cnt]>c:
        dist[p][cnt]=c
        heapq.heappush(edges, (c,p,cnt))
      if dist[p][cnt+1]>cost and cnt<K:
        dist[p][cnt+1]=cost
        heapq.heappush(edges,(cost,p,cnt+1))
  return dist

res = dijk(1)
print(res[N])
print(min(res[N]))
