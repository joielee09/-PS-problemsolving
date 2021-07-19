import sys
import math

sys.stdin = open('input.txt')
n,m = map(int, sys.stdin.readline().split())
tmp = sys.stdin.readline().split()
lis=[]
for item in tmp:
    lis.append(int(item))
# lis = sorted(lis)

def cnt_video(size):
    cnt=0
    tmp_sum=0
    for item in lis:
        if tmp_sum+item>size:
            cnt+=1
            tmp_sum=0
        tmp_sum+=item
    return cnt+1

le = max(lis)
ri = sum(lis)

while le<=ri:
    mid=(le+ri)//2
    cnt=cnt_video(mid)
    if cnt<=m:
        ri=mid-1
    else:
        le=mid+1

print(le)