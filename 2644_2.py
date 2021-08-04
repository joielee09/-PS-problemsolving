# 두 점 간의 거리를 구함

import sys
sys.stdin=open('input.txt')
import heapq

n=int(sys.stdin.readline().strip())
s,e = map(int, sys.stdin.readline().strip().split())
t = int(sys.stdin.readline().strip())
gph =[[0 for _ in range(n+2)] for __ in range(n+2)]
while t:
    t-=1
    p,c = map(int,sys.stdin.readline().strip().split())
    gph[p][c]=1
    gph[c][p]=1

parent=[i for i in range(n+2)]
def find(x,parent):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x],parent)
    return parent[x]

def uni(x,y,parent):
    x = find(x,parent)
    y = find(y, parent)
    if x==y:
        return
    else:
        parent[x]=y
        return


dist=[-1 for _ in range(n+2)]

q=[]
heapq.heappush(q, s)
dist[s]=0

while q:
    cur = heapq.heappop(q)
    for i in range(n+1):
        if gph[cur][i]==1:
            # print(cur, i)
            uni(cur, i, parent)
            if dist[i]!=-1:
                continue
            else:
                heapq.heappush(q,i)
                dist[i] = dist[cur]+1
# print(dist)

# print(parent)

if dist[s]==-1 or dist[e]==-1:
    sys.stdout.write('-1')
else:
    sys.stdout.write(str(abs(dist[s]+dist[e])))