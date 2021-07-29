import sys
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**8)

# @profile
def main():

    n,m = map(int, sys.stdin.readline().strip().split())
    # lis=[0]*(n+2)
    lis=[]
    idx=0

    # @profile
    def binary(tmp, lis):
        if tmp.isdigit():
            tmp = int(tmp)
            lis = sorted(lis, key=lambda x: x[1])
            le = 0
            ri = n+1
            while le<=ri:
                mid = (le+ri)//2
                if lis[mid][1]==tmp:
                    break
                elif lis[mid][1]<tmp:
                    le = mid+1
                else:
                    ri = mid-1
            sys.stdout.write(str(lis[mid][0]))
        else:
            tmp = str(tmp)
            lis = sorted(lis, key=lambda x: x[0])
            le = 0
            ri = n+1
            while le<=ri:
                mid = (le+ri)//2
                if lis[mid][0]==tmp:
                    break
                elif lis[mid][0]<tmp:
                    le = mid+1
                else:
                    ri = mid-1
            sys.stdout.write(str(lis[mid][1]))

    lis.append(("",0))
    while idx<n:
        tmp = sys.stdin.readline().strip()
        # lis[idx] = (tmp, idx)
        lis.append((str(tmp), int(idx)+1))
        idx+=1

    while m:
        m-=1
        tmp = sys.stdin.readline().strip()
        binary(tmp, lis)

if __name__=='__main__':
    main()