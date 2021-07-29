import sys
sys.stdin=open('input.txt')

n=int(sys.stdin.readline())
lis=list(map(int,sys.stdin.readline().split()))
pSum=[]
cnt=0
for n in lis:
    cnt+=n
    pSum.append(cnt)

m=int(sys.stdin.readline())
while m:
    m-=1
    s,e=map(int,sys.stdin.readline().split())
    print(pSum[e-1]-pSum[s-1]+lis[s-1])