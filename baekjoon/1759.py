import sys
sys.stdin = open('input.txt')

l,c = map(int, sys.stdin.readline().split())
lis = sys.stdin.readline().split()
lis = sorted(lis)

consonent=0
vowel=0
answer=[]
tmp=[]
cnt=0

vowel_lis=['a', 'e', 'i', 'o', 'u']
consonent_lis=['b', 'c', 'd', 'f', \
    'g', 'h', 'j', 'k', 'l', 'm', 'n', \
    'p', 'q','r', 's','t','v','w', 'x', 'y', 'z']

def dfs(n):
    global cnt, consonent, vowel
    if len(tmp)==l:
        if consonent>=2 and vowel>=1:
            answer.append(''.join(tmp))

    if n==len(lis):
        return
    dfs(n+1)

    if lis[n] in consonent_lis:
        consonent+=1
    else:
        vowel+=1
    tmp.append(lis[n])
    # print("tmp add: ", n, tmp)
    dfs(n+1)
    if lis[n] in consonent_lis:
        consonent-=1
    else:
        vowel-=1
    tmp.pop(-1)
    # print("tmp off: ", n, tmp)

dfs(0)

# 반례: 중복제거
answer = list(set(answer))
answer = sorted(answer)

for item in answer:
    print(item)