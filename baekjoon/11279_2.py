# https://www.daleseo.com/python-priority-queue/

import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline().strip())
pq=[]
import heapq
# default maxsize: inf
# default order: small->big
while n:
    n-=1
    tmp = int(sys.stdin.readline().strip())
    if tmp==0:
        if len(pq)==0:
            sys.stdout.write('0'+'\n')
        else:
            sys.stdout.write(str((-1*heapq.heappop(pq)))+'\n')
    else:
        heapq.heappush(pq, tmp*(-1))
