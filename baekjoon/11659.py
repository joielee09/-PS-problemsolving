# O(N)을 O(1)에 해결할 수 있음

import sys
sys.stdin=open('input.txt')

n,m=map(int, sys.stdin.readline().split())
lis=list(map(int, sys.stdin.readline().split()))

pSum=[]
cnt=0
for n in lis:
    cnt+=n
    pSum.append(cnt)

while m:
    m-=1
    s,e = map(int, sys.stdin.readline().split())
    print(pSum[e-1]-pSum[s-1]+lis[s-1])