import sys
import heapq

sys.stdin = open("input.txt")

N,M = map(int, sys.stdin.readline().split())
edges=[]
parent=[i for i in range(N+2)]

def find(x, parent):
  if parent[x]==x:
    return x
  parent[x]=find(parent[x], parent)
  return parent[x]

def uni(x,y,parent):
  x = find(x, parent)
  y = find(y, parent)
  if x==y:
    return
  parent[y]=x
  return

while M:
  A, B, C = map(int, sys.stdin.readline().split())
  heapq.heappush(edges, (C,A,B))
  M-=1

cnt=0
answer=0
last_edge=0
while edges:
  w,s,e = heapq.heappop(edges)
  if find(s,parent)!=find(e, parent):
    uni(s,e, parent)
    last_edge = w
    answer+=w
    cnt+=1
  if cnt==N-1:
    break
print(answer-last_edge)
