import sys
sys.stdin=open('input.txt')

@profile
def main():
    n,m = map(int, sys.stdin.readline().strip().split())
    tmp=n
    lis=[]
    while tmp:
        tmp-=1
        num = int(sys.stdin.readline().strip())
        lis.append(num)

    le = 0
    ri = m*min(lis)
    while le<ri:
        cnt=0
        mid = (le+ri)//2

        for i in lis:
            cnt+=(mid//i)
        if cnt<m:
            le = mid +1
        else:
            ri = mid
    sys.stdout.write(str(le))

if __name__=="__main__":
    main()