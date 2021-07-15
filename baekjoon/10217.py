import sys
import heapq
import math
sys.setrecursionlimit(10**8)

sys.stdin=open('input.txt')

T=int(sys.stdin.readline())

def dijk(node, N, M, gph):
  dist=[[math.inf for _ in range(20002)] for __ in range(N+2)]
  edges=[]
  money=0
  dist[node][money]=0
  heapq.heappush(edges, (dist[node][money], node, money))
  while edges:
    cost, pos, money = heapq.heappop(edges)
    if dist[pos][money]<cost:
      continue
    for p,c,m in gph[pos]:
      if money+m>M:
        continue
      c+=cost
      if dist[p][money+m]>c:
        dist[p][money+m]=c
        heapq.heappush(edges, (c,p,money+m))
  return dist

while T:
  T-=1
  N,M,K=map(int, sys.stdin.readline().split())
  k_num=K
  gph=[[] for _ in range(N+2)]
  while k_num:
    k_num-=1
    u,v,c,d=map(int,sys.stdin.readline().split())
    gph[u].append((v,c,d))
  
  res = min(dijk(1, N, M, gph)[N])
  if res==math.inf:
    print("Poor KCM")
  else:
    print(res)