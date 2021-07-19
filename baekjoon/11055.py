import sys

sys.stdin=open('input.txt')

N = int(sys.stdin.readline())
lis = sys.stdin.readline().split()
tmp=[]
for item in lis:
    tmp.append(int(item))
lis=tmp

mm = [x for x in lis]

for i in range(1, N):
    for j in range(i):
        if lis[i]>lis[j]:
            mm[i]=max(mm[i],mm[j]+lis[i])
print(max(mm))