import sys
sys.setrecursionlimit(10**8)
sys.stdin=open('input.txt')

T= int(sys.stdin.readline())

def dp(r,n, mm, lis):
  if mm[r][n]!=-1:
    return mm[r][n]
  mm[r][n] = max( int(lis[r][n])+dp((r+1)%2,n-1,mm,lis), max(dp(r,n-2,mm,lis),dp((r+1)%2,n-2,mm,lis))+int(lis[r][n]) )
  return mm[r][n] 

while T:
  T-=1
  n= int(sys.stdin.readline())
  
  lis=[]
  for _ in range(2):
    lis.append(sys.stdin.readline()[:].split())
  mm=[[-1 for _ in range(n+2)] for __ in range(2)]

  mm[0][0]=int(lis[0][0])
  mm[1][0]=int(lis[1][0])
  mm[0][1]=int(lis[0][1])+mm[1][0]
  mm[1][1]=int(lis[1][1])+mm[0][0]

  res = max(dp(0,n-1,mm,lis), dp(1,n-1,mm,lis))
  # print(mm)
  print(res)