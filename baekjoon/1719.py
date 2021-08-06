import sys
sys.stdin = open('input.txt')
import math
import heapq

n,m = map(int, sys.stdin.readline().strip().split())

gph=[[] for _ in range(n+2)]
for i in range(m):
    s,e,w = map(int, sys.stdin.readline().strip().split())
    gph[s].append((e,w))
    gph[e].append((s,w))

total_dist=[]
total_path=[]
for i in range(1,n+1):
    dist=[math.inf for _ in range(n+2)]
    path=[-1 for _ in range(n+2)]
    edges=[]

    dist[i]=0
    heapq.heappush(edges, (dist[i],i))

    while edges:
        cost,pos = heapq.heappop(edges)
        if dist[pos]<cost:
            continue
        for p,c in gph[pos]:
            c+=cost
            if dist[p]>c:
                dist[p]=c
                heapq.heappush(edges,(c,p))
                path[p]=pos
    total_dist.append(dist)
    total_path.append(path)

# print(total_dist)
# print(total_path)

for i in range(1,n+1):
    for j in range(0,n):
        if i==j+1:
            sys.stdout.write('- ')
        else:
            sys.stdout.write(str(total_path[j][i])+' ')
    sys.stdout.write('\n')