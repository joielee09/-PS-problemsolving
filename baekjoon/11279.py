# https://www.daleseo.com/python-priority-queue/
# max size를 지정할 때 heapq와 속도차이 체크
import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline().strip())

from queue import PriorityQueue
# default maxsize: inf
# default order: small->big
pq = PriorityQueue(maxsize=n+2) 
while n:
    n-=1
    tmp = int(sys.stdin.readline().strip())
    if tmp==0:
        if pq.empty():
            sys.stdout.write('0'+'\n')
        else:
            sys.stdout.write(str((-1*pq.get()))+'\n')
    else:
        pq.put(tmp*(-1))
