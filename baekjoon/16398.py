# 최소한의 비용으로 모든 행성을 잇는 간선을 만든다

import sys
sys.stdin=open('input.txt')
import heapq
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline().strip())

gph=[]
for i in range(n):
    gph.append(list(map(int, sys.stdin.readline().strip().split())))



parent=[i for i in range(n+2)]

def find(x, parent):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x], parent)
    return parent[x]

def uni(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    if x==y:
        return
    else:
        parent[x]=y
        return

edges=[]
for i in range(n):
    for j in range(n):
        heapq.heappush(edges, (gph[i][j], i, j))
cnt=0
answer=0
while edges:
    w,s,e = heapq.heappop(edges)
    if find(s, parent)!=find(e,parent):
        uni(s,e,parent)
        answer+=w
        cnt+=1
    if cnt==n-1:
        break

sys.stdout.write(str(answer))
