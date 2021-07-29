import sys
sys.stdin=open('input.txt')

n,m=map(int, sys.stdin.readline().strip().split())
dic={}

for i in range(1,n+1):
    a = sys.stdin.readline().strip()
    dic[i]=a
    dic[a]=i

for i in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(dic[int(q)])
    else:
        print(dic[str(q)])
