import sys
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**8)

# @profile
def main():

    n,m = map(int, sys.stdin.readline().strip().split())
    # lis=[0]*(n+2)
    lis=[]
    lis_digit=[0]*(n+2)
    idx=0

    # @profile
    def binary(tmp, lis):
        tmp = str(tmp)
        le = 0
        ri = n+1
        while le<=ri:
            mid = (le+ri)//2
            if lis[mid][0]==tmp: # 정확한 값을 찾을 때는 ==조건
                break
            elif lis[mid][0]<tmp:
                le = mid+1
            else:
                ri = mid-1
        return lis[mid][1]

    lis.append(("",0)) # item의 번호가 1번부터 시작해서 필요
    while idx<n:
        tmp = sys.stdin.readline().strip()
        lis.append((str(tmp), int(idx)+1))
        lis_digit[int(idx)]=str(tmp)
        idx+=1
    lis = sorted(lis, key=lambda x: x[0]) # 정렬 때문에 시간초과, key lambda 정렬에는 append로 넣어야한다.

    while m:
        m-=1
        tmp = sys.stdin.readline().strip()
        if tmp.isdigit():
            sys.stdout.write(str(lis_digit[int(tmp)-1])+'\n')
        else:
            ans = binary(tmp, lis)
            sys.stdout.write(str(ans)+'\n')

if __name__=='__main__':
    main()