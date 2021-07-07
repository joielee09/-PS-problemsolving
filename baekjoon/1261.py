import sys
import heapq
import math

sys.stdin=open('input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def valid(r,c,n,m):
  return r>=0 and c>=0 and r<n and c<m

M,N=map(int, sys.stdin.readline().split())
lis=[]
for i in range(N):
    num = sys.stdin.readline()
    tmp=[]
    for j in range(len(num)):
      if num[j]=='\n':
        continue
      tmp.append(int(num[j]))
    lis.append(tmp)
# print(lis)

dist=[[math.inf for _ in range(M)] for __ in range(N)]
edges=[]

dist[0][0]=0
heapq.heappush(edges, (dist[0][0],0,0))

while edges:
  weight,curR,curC = heapq.heappop(edges)
  for idx in range(4):
    nextR = curR+dr[idx]
    nextC = curC+dc[idx]
    if not valid(nextR,nextC,N,M):
      continue
    if dist[nextR][nextC]>dist[curR][curC]+lis[nextR][nextC]:
      dist[nextR][nextC]=dist[curR][curC]+lis[nextR][nextC]
      heapq.heappush(edges, (dist[nextR][nextC],nextR,nextC))

# print(dist)
print(dist[N-1][M-1])