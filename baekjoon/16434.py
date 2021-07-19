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
    # res = play(atk, mid)
    cur_hp, cur_atk = mid, atk
    # print(mid, res)
    for item in lis:
        t,a,h = item[0], item[1], item[2]
        if t==1:
            cur_hp-=(math.ceil(h/cur_atk)-1)*a
            if cur_hp<1:
                break
        else:
            cur_atk+=a
            cur_hp=min(cur_hp+item[2], mid)
    if cur_hp<1:
        le=mid+1
    else:
        ri=mid-1
print(le)
