import sys
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**7)

class node:
    def __init__(self):
        self.left=0
        self.right=0
        self.depth=0
        self.order=0

max_depth=-1
order=0

# @profile
def main():
    N=int(sys.stdin.readline())
    gph=[node() for _ in range(N+2)]
    root=[0]*(N+2)
    left=[0]*(N+2)
    right=[0]*(N+2)

    n=N
    while n:
        n-=1
        num, le, ri = map(int, sys.stdin.readline().split())
        gph[num].left=le
        gph[num].right=ri
        if le!=-1:
            root[le]=1
        if ri!=-1:
            root[ri]=1


    def inorder(node, depth):
        global order, max_depth
        if node==-1:
            return
        left = gph[node].left
        right = gph[node].right
        inorder(left, depth+1)
        gph[node].depth=depth
        max_depth = max(max_depth, depth)
        order+=1
        gph[node].order=order
        inorder(right, depth+1)

    root_idx=-1
    for idx in range(1,N+1):
        if root[idx]==0:
            root_idx = idx

    inorder(root_idx, 1)

    left_min=[0]*(N+2)
    right_max=[0]*(N+2)
    for idx in range(1,N+1):
        depth=gph[idx].depth
        if left_min[depth]==0:
            left_min[depth]=gph[idx].order
        if right_max[depth]==0:
            right_max[depth]=gph[idx].order
        left_min[depth] = min(left_min[depth], gph[idx].order)
        right_max[depth] = max(right_max[depth], gph[idx].order)

    answer_wdith=-1
    answer_depth=-1

    tmp_wid=-1
    for idx in range(1, max_depth+1):
        wid= right_max[idx]-left_min[idx]+1
        if wid>tmp_wid: #갱신한다면
            answer_depth=idx
            answer_wdith=wid
            tmp_wid=wid
    sys.stdout.write(str(answer_depth)+' '+str(answer_wdith))
    # print(answer_wdith, answer_depth)

if __name__ == "__main__":
    main()