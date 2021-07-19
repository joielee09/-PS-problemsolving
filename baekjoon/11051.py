import sys
sys.stdin = open('input.txt')

N,K = map(int, sys.stdin.readline().split())
mod = 10**4+7

mm = [[0 for _ in range(N+2)] for __ in range(N+2)]
for i in range(N+1):
    mm[i][0]=1

for i in range(1, N+1):
    for j in range(1, i+1):
        mm[i][j]= mm[i-1][j-1]+mm[i-1][j]

print(mm[N][K]%mod)