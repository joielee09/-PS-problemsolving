import sys
sys.stdin = open('input.txt')

import heapq
lis = []
n = int(sys.stdin.readline().strip())

while n:
    n-=1
    tmp = int(sys.stdin.readline().strip())
    if tmp==0:
        if len(lis)==0:
            sys.stdout.write('0')
        else:
            sys.stdout.write(str(heapq.heappop(lis)))
        sys.stdout.write('\n')
    else:
        heapq.heappush(lis, tmp)
