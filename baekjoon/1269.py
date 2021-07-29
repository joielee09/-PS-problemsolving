# https://simsimjae.tistory.com/214
import sys
sys.stdin =open('input.txt')

# @profile
def main():
    a,b=map(int, sys.stdin.readline().strip().split())
    a_lis = list(map(int, sys.stdin.readline().strip().split()))
    b_lis = list(map(int, sys.stdin.readline().strip().split()))

    lis_a = sorted(a_lis)
    lis_b = sorted(b_lis)

    # @profile
    def binary(lis, n):
        # if lis == 'A':
        #     le = 0
        #     ri = b-1
        # else:
        #     le = 0
        #     ri = a-1
        le = 0
        ri = len(lis)-1

        while le<=ri:
            mid = (le+ri)//2
            if lis[mid]==n:
                return 1
            if lis[mid]<n:
                le = mid+1
            else:
                ri = mid-1
            # if lis == 'A':
            #     if lis_b[mid]==n:
            #         return 1
            #     if lis_b[mid]<n:
            #         le = mid+1
            #     else:
            #         ri = mid-1
            # if lis == 'B':
            #     if lis_a[mid]==n:
            #         return 1
            #     if lis_a[mid]<n:
            #         le = mid+1
            #     else:
            #         ri = mid-1
        return 0

    answer=0
    cnt=0
    for item in a_lis:
        cnt+=binary(lis_b, item)
    answer+=(a-cnt)
    cnt=0
    for item in b_lis:
        cnt+=binary(lis_a, item)
    answer+=(b-cnt)

    sys.stdout.write(str(answer))

if __name__=="__main__":
    main()
