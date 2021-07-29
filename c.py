import sys
import math
import copy
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**8)

n, atk = map(int, sys.stdin.readline().split())

lis=[]
while n:
    n-=1
    [t,a,h] = map(int, sys.stdin.readline().split())
    lis.append([t,a,h])

def play(atk, hp):
    max_hp=hp
    cur_atk = atk
    for item in lis:
        # print(item, "hp: ", hp, cur_atk)
        cur_item = copy.deepcopy(item)
        if cur_item[0]==1: # dragon
            # while True:
            #     # print("fight: " ,hp, cur_item[2])
            #     cur_item[2]-=cur_atk
            #     if cur_item[2]<1:
            #         break
            #     hp-=cur_item[1]
            #     if hp<1:
            #         return hp
            hp-=((math.ceil(cur_item[2]/cur_atk)-1)*cur_item[1])
            if hp<1:
                return hp
        else: # portion
            cur_atk+=item[1]
            hp=min(hp+item[2], max_hp)
    
    return hp

le = 1
ri = 10**18

while le<=ri:
    mid=(le+ri)//2
    res = play(atk, mid)
    # print(mid, res)
    if res<1:
        le=mid+1
    else:
        ri=mid-1
print(le)
