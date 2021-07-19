import sys
sys.stdin = open('input.txt')

n,m =map(int,sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))

le=1
ri=max(lis)

while le<=ri:
    mid = (le+ri)//2
    total= [tree-mid if tree>mid else 0 for tree in lis]
    # print(total)
    total_val = sum(total)
    # for tree in lis:
    #     if tree>mid:
    #         total+=(tree-mid)
    if total_val>=m:
        le=mid+1
    else:
        ri=mid-1

print(ri)