import sys
import math

sys.stdin=open('input.txt')

N=int(sys.stdin.readline())
mm=[math.inf]*int(N+2) #최소 math.inf
mm[0]=0
mm[1]=1
sqr=[i*i for i in range(1,int(N**0.5)+1)]

for i in range(1,N+2):
    tmp=[]
    for j in sqr:
        if i<j:
            break
        tmp.append(mm[i-j]+1)
    mm[i] = min(tmp)

if mm[N]==math.inf:
    print(-1)
else:
    print(mm[N])
