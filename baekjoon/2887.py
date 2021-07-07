import sys
import heapq

sys.stdin = open("input.txt")

N = int(sys.stdin.readline())

lis=[]
for i in range(N):
  x,y,z=map(int,sys.stdin.readline().split())
  lis.append((x,y,z,i))
# print(lis)
parent=[i for i in range(N+2)]

def find(x,parent):
  if parent[x]==x:
    return x
  parent[x]=find(parent[x],parent)
  return parent[x]

def uni(x,y,parent):
  x=find(x,parent)
  y=find(y,parent)
  if x==y:
    return
  parent[y]=x
  return

edges=[]
for i in range(3):
  lis.sort(key=lambda x:x[i])
  for idx in range(len(lis[:-1])):
    w = abs(lis[idx][i]-lis[idx+1][i])
    heapq.heappush(edges, (w,lis[idx][3],lis[idx+1][3]))

answer=0
cnt=0
while edges:
  cur = heapq.heappop(edges)
  if find(cur[1], parent)!=find(cur[2],parent):
    uni(cur[1],cur[2],parent)
    answer+=cur[0]
    cnt+=1

print(answer)