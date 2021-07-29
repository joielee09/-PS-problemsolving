import sys
sys.stdin=open('input.txt')

N = int(sys.stdin.readline())

def valid(s):
    for i in range(1, len(s)//2+1):
        if s[-2*i:-1*i]==s[-1*i:]: #indexing
            return False
    return True

s=""
answer=[]
def dfs(s):
    if len(s)==N:
        print(s)
        exit() #exit
    for i in '123': #indexing
        if valid(s+str(i)):
            dfs(s+str(i))
    return
dfs('1')