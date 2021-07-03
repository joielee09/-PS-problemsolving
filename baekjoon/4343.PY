import sys
import heapq

sys.stdin = open("input.txt")
t = int(sys.stdin.readline())

def find(x, parent):
  if parent[x]==x:
    return x
  parent[x] = find(parent[x],parent)
  return parent[x]

def uni(x,y,parent):
  x = find(x, parent)
  y = find(y, parent)
  if x==y:
    return
  else:
    parent[y]=x
  return

while t:

  S,P = map(int, sys.stdin.readline().split())
  P_=P
  edges = []
  parent = [i for i in range(P+2)]
  satellites = [list(map(int, sys.stdin.readline().split())) for _ in range(P)]

  for i in range(len(satellites)):
    for j in range(i+1,len(satellites)):
      if i==j:
        continue
      p1 = satellites[i]
      p2 = satellites[j]
      w = round(((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5,2)
      heapq.heappush(edges, (w,i,j))
  # print(edges)
  cnt=0
  weight_lis=[]
  res=0
  while True:
    w,s,e = heapq.heappop(edges)
    if find(s, parent)!=find(e, parent):
      uni(s,e,parent)
      res=w
      cnt+=1
    if cnt==P-S:
      break
  # print(weight_lis)
  print('%.2f'%res)
  t-=1
