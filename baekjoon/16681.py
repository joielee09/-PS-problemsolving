import heapq
import math
import sys

sys.stdin = open("input.txt")

N,M,D,E = map(int, sys.stdin.readline().split())
h_lis = list(map(int, sys.stdin.readline().split()))

gph=[[] for _ in range(N+2)]
while M:
  M-=1
  a,b,c =map(int,sys.stdin.readline().split())
  gph[a].append((b,c))
  gph[b].append((a,c))
# print(gph)

def dijkstra(node):
    dist=[math.inf for i in range(N+2)]
    edges=[]

    dist[node]=0
    heapq.heappush(edges,(0,node))

    cnt=0
    while edges:
        cost,pos = heapq.heappop(edges)
        # 다익스트라에서 시간초과 처리하는 방법.
        # if dist[pos]<cost:
        #     continue
        for p,c in gph[pos]:
            if h_lis[p-1]<=h_lis[pos-1]: # 다음이 낮아지는 방향이면 방문하지 않는다.
                continue
            c+=cost 
            if dist[p]>c:
                dist[p]=c
                heapq.heappush(edges,(c,p))
                cnt+=1
        # MST에서 처리
        # if cnt==N+1:
        #     break
    return dist

home_short = dijkstra(1)
school_short = dijkstra(N)

answer = []
for i in range(1,N+1):
    if home_short[i] != math.inf and school_short[i] != math.inf:
        answer.append(h_lis[i-1] * E - (home_short[i] + school_short[i]) * D)
print(max(answer) if answer else 'Impossible')