import sys
sys.stdin = open('input.txt')

k,n = map(int, sys.stdin.readline().split())
lis=[]
while k:
    k-=1
    lis.append(int(sys.stdin.readline()))

le = 1
ri = max(lis)

while le<=ri:
    mid = (le+ri)//2
    total=0
    for item in lis:
        total+=(item//mid)
    if total<n:
        ri=mid-1
    else:
        le=mid+1
print(ri)