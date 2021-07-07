import sys
import heapq
import math

sys.stdin=open('input.txt')

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def valid(r,c,len):
  return r>=0 and c>=0 and r<len and c<len

t=0
while True:
  t+=1
  n=int(sys.stdin.readline())
  if n==0:
    break
  cnt=n
  lis=[]
  while cnt:  
    lis.append(list(map(int, sys.stdin.readline().split())))
    cnt-=1
  
  dist=[[math.inf for _ in range(n)] for __ in range(n)]
  edges=[]

  dist[0][0]=lis[0][0]
  heapq.heappush(edges, (dist[0][0],0,0))

  while edges:
    weight,curR,curC = heapq.heappop(edges)
    for idx in range(4):
      nextR = curR+dr[idx]
      nextC = curC+dc[idx]
      if not valid(nextR,nextC,n):
        continue
      if dist[nextR][nextC]>dist[curR][curC]+lis[nextR][nextC]:
        dist[nextR][nextC]=dist[curR][curC]+lis[nextR][nextC]
        heapq.heappush(edges, (dist[nextR][nextC],nextR,nextC))

  print(f"Problem {t}: {dist[n-1][n-1]}")