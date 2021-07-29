import sys
sys.stdin=open('input.txt')

import heapq
answer=[]

n,m = map(int, sys.stdin.readline().strip().split())
lis = list(map(int, sys.stdin.readline().strip().split()))
q = lis
heapq.heapify(q)

for i in range(m+1):
    cur = heapq.heappop(q)
    for j in lis:
        heapq.heappush(q, cur*j)
print(list(s))