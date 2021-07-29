import sys
sys.stdin=open('input.txt')

n, m=map(int, sys.stdin.readline().split())
lis=list(map(int,sys.stdin.readline().split()))

pSum=[]
cnt=0
answer=0
res=[0]*(m+1)

for n in lis:
    cnt+=n
    res[cnt%m]+=1
    
answer+=res[0]
for item in res:
    answer+=((item*(item-1))//2)
print(answer)