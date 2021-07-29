import sys
import math
import copy
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**8)

# 방의 갯수와 처음 전투력
n, atk = 3 ,3

# 각 방에 관한 정보
lis=[[1,1,20],[2,3,10],[1,3,100]]

@profile
def play(atk, hp):
    max_hp=hp
    cur_atk = atk
    for item in lis:
        # print(item, "hp: ", hp, cur_atk)
        cur_item = copy.deepcopy(item)
        if cur_item[0]==1: # dragon
            hp-=((math.ceil(cur_item[2]/cur_atk)-1)*cur_item[1])
            if hp<1:
                return hp
        else: # portion
            cur_atk+=item[1]
            hp=min(hp+item[2], max_hp)
    
    return hp

@profile
def problem():

    le = 1
    ri = 10**18

    while le<=ri:
        mid=(le+ri)//2

        cur_hp, cur_atk = mid, atk

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

problem()