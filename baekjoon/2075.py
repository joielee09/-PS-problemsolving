import sys
sys.stdin = open('input.txt')
import heapq

n = int(sys.stdin.readline().strip())
lis=[]

# first list
tmp = list(map(int, sys.stdin.readline().strip().split()))
for item in tmp:
    heapq.heappush(lis, item)

# other list
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    for item in tmp:
        heapq.heappush(lis, item)
        heapq.heappop(lis)
print(lis[0])