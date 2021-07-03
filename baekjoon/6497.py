import sys
import heapq
# sys.stdin = open("input.txt")

def find(x, parent):
  if parent[x]==x:
    return x
  else:
    parent[x] = find(parent[x],parent)
    return parent[x]

def uni(x,y,parent):
  x = find(x,parent)
  y = find(y,parent)
  if x==y:
    return
  else:
    parent[y] = x
  return

while True:
  m,n = map(int, sys.stdin.readline().split())
  if (m,n)==(0,0):
    break
  
  edges = []
  parent = [ i for i in range(m+2)]
  total = 0

  while n:
    x,y,z = map(int, sys.stdin.readline().split())
    total+=z
    heapq.heappush(edges, (z,x,y))
    n-=1

  answer = 0
  cnt=0
  while True:
    w,s,e = heapq.heappop(edges)
    if find(s, parent)!=find(e, parent):
      uni(s,e,parent)
      answer+=w
      cnt+=1
    if cnt==m-1:
      break

  print(total-answer)