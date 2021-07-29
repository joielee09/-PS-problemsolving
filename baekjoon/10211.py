import sys
import math
sys.stdin = open('input.txt')

t = int(sys.stdin.readline())
while t:
    t-=1
    n = int(sys.stdin.readline())
    lis = list(map(int, sys.stdin.readline().split()))
    pSum=[]
    cnt=0
    for item in lis:
        cnt+=item
        pSum.append(cnt)
    max_val=-math.inf
    for i in range(len(pSum)):
        for j in range(i, len(pSum)):
            max_val = max(pSum[j]-pSum[i]+lis[i], max_val)
    sys.stdout.write(str(max_val)+'\n')
    # print(max_val)