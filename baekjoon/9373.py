import sys
import heapq

sys.stdin=open("input.txt")
sys.setrecursionlimit(5000)

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

t = int(sys.stdin.readline())
while t:
  t-=1
  w = int(sys.stdin.readline())
  num=int(sys.stdin.readline())
  lis=[]
  edges=[]
  answer=0
  
  lis=[list(map(int, sys.stdin.readline().split()))+[i] for i in range(num)]

  parent=[i for i in range(num+2)]

  d=100002
  for i in range(len(lis)):
    dist = lis[i][0]-lis[i][2]
    if dist>0:
      d = min(d,dist)
    else:
      uni(i,num,parent)
  if parent[i]!=parent[num]:
    heapq.heappush(edges,(dist,i,num))
  
  d=100002
  for i in range(len(lis)):
    dist = w-(lis[i][0]+lis[i][2])
    if dist>0:
      d = min(d,dist)
    else:
      uni(i,num+1,parent)
  if parent[i]!=parent[num+1]:
    heapq.heappush(edges,(dist,i,num+1))
  
  for i in range(len(lis)):
    for j in range(i+1,len(lis)):
      if i==j:
        continue
      p1 = lis[i]
      p2 = lis[j]
      w= ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5-p1[2]-p2[2]
      # print("w:" ,w)
      if w>0:
        heapq.heappush(edges,(w,i,j))
      else:
        uni(i,j,parent)
  # print(edges)
  ans=10002
  cnt=0
  if find(num, parent)==find(num+1, parent):
      print(0)
  else:
    while edges:
      cur = heapq.heappop(edges)
      # print(cur)
      if find(cur[1],parent)!=find(cur[2],parent):
        uni(cur[1],cur[2],parent)
        ans=min(ans,cur[0])
      if find(num, parent)==find(num+1, parent):
        break
    # sys.stdout.write("%.6f\n"%(ans/2))
    print(round(ans/2,6))

