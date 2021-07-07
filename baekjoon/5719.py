import sys
import heapq
import math
from collections import deque
sys.setrecursionlimit(1000000)

# sys.stdin = open("almost.in")
sys.stdin = open("input.txt")

def dijk(node, gph):

  dist=[math.inf for _ in range(N+2)]
  edges=[]

  dist[node] = 0
  heapq.heappush(edges,(dist[node], node))

  while edges:
    cost, pos = heapq.heappop(edges)
    if dist[pos]<cost:
      continue
    for p,c in gph[pos]:
      c+=cost
      if dist[p]>c:
        dist[p]=c
        heapq.heappush(edges,(c, p))
  return dist

while True:
  N, M = map(int, sys.stdin.readline().split())
  if (N,M)==(0,0):
    break
  S, D = map(int, sys.stdin.readline().split())

  dist=[math.inf for _ in range(N+2)]
  edges=[]
  gph=[[] for _ in range(N)]
  back_gph=[[] for _ in range(N)]
  adj = [[-1 for i in range(N)] for j in range(N)]

  while M:
    M-=1
    u,v,p = map(int, sys.stdin.readline().split())
    gph[u].append((v,p))
    back_gph[v].append((u,p))
    adj[u][v]=p

  res_lis = dijk(S,gph)
  res =res_lis[D]

  visit=[[-1 for _ in range(N)] for __ in range(N)]
  q=deque()
  s=set()
  q.append(D)
  
  while q:
    cur = q.popleft()
    for (p,c) in back_gph[cur]:
      if visit[cur][p]==1:
        continue
      if res_lis[cur] == res_lis[p]+c:
        s.add((p,cur)) # 바로 gph에 사용할 수 있게!
        q.append(p)
        if p==S:
          continue
        else:
          visit[cur][p]=1
  
  gph_=[[] for _ in range(N)]
  for u,v in s:
    adj[u][v]=-1
  for i in range(N):
    for j in range(N):
      if adj[i][j]!=-1:
        gph_[i].append((j,adj[i][j]))

  res_lis = dijk(S,gph_)

  if res_lis[D] == math.inf:
    print(-1)
  else:
    print(res_lis[D])