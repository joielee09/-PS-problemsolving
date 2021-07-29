import sys
sys.stdin = open('input.txt')

R,C = map(int, sys.stdin.readline().split())
lis= [[ord(x)-65 for x in input()] for _ in range(R)]

# don't need this
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer=1
ch = [0]*26

def valid(r,c):
    return (0<=r and r<R and 0<=c and c<C)

def dfs(r,c,mv):
    global answer
    answer = max(answer, mv)

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if not valid(nr,nc):
            continue
        if ch[lis[nr][nc]]==1:
            continue

        ch[lis[nr][nc]]=1
        dfs(nr,nc, mv+1)
        ch[lis[nr][nc]]=0

ch[lis[0][0]]=1
dfs(0,0, answer)
print(answer)