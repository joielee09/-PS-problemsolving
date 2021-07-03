import sys
import heapq

# sys.stdin = open("input.txt")

n = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
edges=[]

parent=[i for i in range(n+2)]

def find(x, parent):
  if parent[x]==x:
    return x
  parent[x] = find(parent[x], parent)
  return parent[x]

def uni(x,y, parent):
  x = find(x, parent)
  y = find(y, parent)
  if x==y:
    return
  else:
    parent[x]=y
  return

while edge:
  s,e,w = map(int, sys.stdin.readline().split())
  heapq.heappush(edges, (w,s,e))
  edge-=1

answer=0

while edges:
  w,s,e = heapq.heappop(edges)
  # print(w,s,e)
  if find(s,parent) != find(e,parent):
    uni(s,e,parent)
    answer+=w

print(answer)