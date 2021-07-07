import sys
import heapq
import math

sys.stdin = open('generated098.in')

sr,sc=map(float, sys.stdin.readline().split())
dr,dc=map(float, sys.stdin.readline().split())
n = int(sys.stdin.readline())

def distance(curR,curC,nextR,nextC):
  return ((curR-nextR)**2+(curC-nextC)**2)**0.5

def dijk(node, gph):

  dist=[math.inf for _ in range(len(canon))]
  edges=[]
  
  dist[node]=0
  heapq.heappush(edges, (dist[node], node)) # cost, pos
  
  while edges:
    cost,pos = heapq.heappop(edges)
    if dist[pos]<cost:
      continue
    for p, c in enumerate(gph[pos]):
      # print(pos,p,c)
      c +=cost
      if dist[p]>c:
        dist[p]=c
        heapq.heappush(edges, (c,p))
  return dist

canon=[]
canon.append((sr,sc))

while n:
  n-=1
  cr, cc = map(float, sys.stdin.readline().split())
  canon.append((cr,cc))
canon.append((dr,dc))

time =[ [] for _ in range(len(canon))]
for i in range(len(canon)):
  for j in range(len(canon)):
    if i==0 or i==len(canon)-1:
      time[i].append(distance(canon[i][0], canon[i][1], canon[j][0], canon[j][1])/5) # 걸어가는 시간
    else:
      time[i].append(abs(distance(canon[i][0], canon[i][1], canon[j][0], canon[j][1])-50)/5+2) # 대포 한 번 + 걸어가기 

# print(time)
res = dijk(0,time)
print(res[len(canon)-1])