# 두 점 간의 거리를 구함
# union find에서 문제나는 부분 기억!!!

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
    y = find(y,parent)
    if x==y:
        return
    else:
        parent[x]=y
        return


dist=[-1 for _ in range(n+2)]
for iter in range(1, n+1):
    if dist[iter]!=-1:
        continue
    q=[]
    heapq.heappush(q, iter)
    dist[iter]=0

    while q:
        cur = heapq.heappop(q)
        for i in range(n+1):
            if gph[cur][i]==1:
                uni(cur, i, parent)
                if dist[i]!=-1:
                    continue
                else:
                    heapq.heappush(q,i)
                    dist[i] = dist[cur]+1

for i in range(1,n):
    if find(i,parent)==find(i+1, parent):
        uni(i,i+1, parent)

if parent[s]!=parent[e]:
    sys.stdout.write('-1')
else:
    sys.stdout.write(str(abs(dist[s]+dist[e])))