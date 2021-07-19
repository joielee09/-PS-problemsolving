import sys
sys.stdin=open('input.txt')

N=int(sys.stdin.readline())
tmp=sys.stdin.readline().split(' ')
lis = [0]*(N+5)
for idx, elem in enumerate(tmp):
    lis[idx+1] = int(elem)

mm=[0]*(N+5)
for i in range(1,N+2):
    tmp=[]
    for j in range(0, i+1):
        tmp.append(lis[i-j]+mm[j])
    mm[i]=max(tmp)
print(mm[N])