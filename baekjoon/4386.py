import sys
import heapq

sys.stdin = open("input.txt")

n = int(sys.stdin.readline())
edges=[]
parent=[i for i in range(n+2)]
stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

def find(x, parent):
  if parent[x]==x:
    return x
  parent[x] = find(parent[x],parent)
  return parent[x]

def uni(x,y,parent):
  x = find(x,parent)
  y = find(y,parent)
  if x==y:
    return
  parent[y]=x
  return

for i in range(len(stars)):
  for j in range(len(stars)):
    if i==j:
      continue
    p1 = stars[i]
    p2 = stars[j]
    w = round(((p1[0]-p2[0])**2+abs(p1[1]-p2[1])**2)**0.5, 2)
    heapq.heappush(edges, (w,p1,p2,i,j))

answer=0
while edges:
  w,s,e,i,j = heapq.heappop(edges)
  if find(i, parent)!=find(j, parent):
    uni(i,j, parent)
    answer+=w

print(answer)