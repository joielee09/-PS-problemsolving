import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

le=0
ri=max(lis)
sum=0
while le<=ri:
    mid = (le+ri)//2
    sum=0
    for item in lis:
        sum +=min(item, mid)
    if sum>m:
        ri=mid-1
    else:
        le=mid+1
# print(sum)
print(ri)
