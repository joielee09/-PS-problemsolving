import sys
sys.stdin = open('input.txt')

sys.setrecursionlimit(10**8)

# @profile
def main():
    n = int(sys.stdin.readline())
    tree=[[] for _ in range(n+2)]
    tmp=n
    while tmp>1:
        tmp-=1
        n_1, n_2 = map(int, sys.stdin.readline().split())
        tree[n_1].append(n_2)
        tree[n_2].append(n_1)

    root_lis=[0]*(n+2)
    def find_root(root):
        for item in tree[root]:
            if root_lis[item]==0:
                root_lis[item]=root
                find_root(item)
        return
    find_root(1)
    for idx in range(2,n+1):
        sys.stdout.write(str(root_lis[idx])+'\n')

if __name__=="__main__":
    main()