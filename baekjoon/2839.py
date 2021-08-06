import sys
sys.stdin = open('input.txt')
import math

target = int(sys.stdin.readline().strip())
lis = [math.inf]*5002
lis[3] = 1
lis[5] = 1

for i in range(6, target+1):
    lis[i] = min(lis[i-3]+1, lis[i-5]+1)

if lis[target]==math.inf:
    print(-1)
else:
    print(lis[target])