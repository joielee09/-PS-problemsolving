import sys
sys.stdin=open('input.txt')

M = int(sys.stdin.readline())

s = set()
while M:
    M-=1
    cmd = sys.stdin.readline().split()
    if len(cmd)==1:
        c = cmd[0]
    else:
        c = cmd[0]
        n = int(cmd[1])

    if c=='add':
        s.add(n)
    elif c=='check':
        if n in s:
            print(1)
        else:
            print(0)
    elif c=='remove':
        s.discard(n)
    elif c=='toggle':
        if n in s:
            s.discard(n)
        else:
            s.add(n)
    elif c=='all':
        s=set([i for i in range(1,21)])
    else: # empty
        s = set()
