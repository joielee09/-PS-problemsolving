import sys
sys.stdin=open('input.txt')
from collections import deque
mod = 10**4+7

N=int(sys.stdin.readline())
mm=[[1]*(10) for _ in range(N+2)]

for i in range(2,N+1): # i: 길이, j: 숫자
    mm[i][9]=mm[i-1][9]
    for j in range(0,9):
        for k in range(0,j+1):
            mm[i][j] += mm[i-1][j-k]

print(sum(mm[N])%mod)