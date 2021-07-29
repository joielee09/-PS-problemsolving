import sys
sys.stdin = open('input.txt')

n,m = map(int, sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))

cnt=0
curSum=0

def dfs(cur):
    global cnt, curSum
    if cur==n:
        return
    if curSum+lis[cur]==m:
        cnt+=1
    dfs(cur+1)
    curSum+=lis[cur]
    dfs(cur+1)
    curSum-=lis[cur]

dfs(0)
print(cnt)