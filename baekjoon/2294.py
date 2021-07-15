import sys
import math

sys.stdin=open('input.txt')

n,k = map(int, sys.stdin.readline().split())
coins=[]
while n:
    n-=1
    c = int(sys.stdin.readline())
    coins.append(c)
coins.sort()

mm=[math.inf]*int(k+2)
mm[0]=0

for i in range(k+1):
    for j in coins:
        if i<j:
            break
        mm[i]=min(mm[i],mm[i-j]+1)

if mm[k]==math.inf:
    print(-1)
else:
    print(mm[k])