import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)
dx=[0,1,0,-1]
dy=[-1,0,1,0]

n,m = map(int, sys.stdin.readline().strip().split())
startR, startC, di = map(int, sys.stdin.readline().strip().split())

g=[]
for i in range(n):
    g.append(list(map(int, sys.stdin.readline().strip().split())))
visit = [[0 for _ in range(m)] for __ in range(n)]

def valid(r,c):
    return r>=0 and c>=0 and r<n and c<m

circle=[[3,2,1,0], [0,3,2,1], [1,0,3,2], [2,1,0,3]]
back_dir = {0:2, 1:3, 2:0, 3:1}
max_val=0

return_flag=False
def dfs(r,c,d):
    global return_flag
    # print(return_flag)
    # print("currnet: ", r,c,d)
    # print(visit)
    nextDir = -1
    # print(circle[d])
    cnt=0
    
    if return_flag==True:
        return
    for i in circle[d]:
        nextDir = i
        if return_flag==True:
            break
        # print(dy[i], dx[i])
        nextR = r+dy[i]
        nextC = c+dx[i]
        # print("next: ", nextR, nextC)
        if not valid(nextR, nextC):
            # print("cnt: ", cnt)
            cnt+=1
            if cnt==4:
                
                nextR = r+dx[back_dir[d]]
                nextC = c+dy[back_dir[d]]
                # print("next: ", nextR, nextC)
                if g[nextR][nextC]==1:
                    # print("hit the wall")
                    return_flag=True
                    return
                else:
                    dfs(nextR,nextC,d)
            continue
        if g[nextR][nextC]==1:
            # print("cnt: ", cnt)
            cnt+=1
            if cnt==4:
                # print("d",d)
                nextR = r+dy[back_dir[d]]
                nextC = c+dx[back_dir[d]]
                # print("next: ", nextR, nextC)
                if g[nextR][nextC]==1:
                    return_flag=True
                    # print("hit the wall")
                    return
                else:
                    dfs(nextR,nextC,d)
            continue
        if visit[nextR][nextC]!=0:
            # print("cnt: ", cnt)
            cnt+=1
            if cnt==4:
                # print("d",d)
                nextR = r+dy[back_dir[d]]
                nextC = c+dx[back_dir[d]]
                # print("next: ", nextR, nextC)
                if g[nextR][nextC]==1:
                    return_flag=True
                    # print("hit tree here")
                    return
                else:
                    dfs(nextR,nextC,d)
            continue
        visit[nextR][nextC]=visit[r][c]+1
        dfs(nextR,nextC,nextDir)
    return

visit[startR][startC]=1
dfs(startR, startC, di)
# print(visit)

answer=0
for i in range(n):
    for j in range(m):
        if visit[i][j]!=0:
            answer+=1
print(answer)