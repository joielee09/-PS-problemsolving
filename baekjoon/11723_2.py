import sys
sys.stdin=open('input.txt')

M = int(sys.stdin.readline())
bit=0

while M:
    M-=1
    cmd = sys.stdin.readline().split()
    
    if len(cmd)==1:
        c = cmd[0]
    else:
        c = cmd[0]
        n = int(cmd[1])-1

    if c=='add':
        bit = bit|(1<<n)
    elif c=='remove':
        bit = bit& ~(1<<n)
    elif c=='check':
        if bit & (1<<n)==0:
            print(0)
        else:
            print(1)
    elif c=='toggle':
        bit = bit^(1<<n)
    elif c=='all':
        bit = (1<<20)-1
    else: # empty
        bit =0
