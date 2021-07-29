import sys
sys.stdin=open('input.txt')
import heapq

t = int(sys.stdin.readline().strip())
while t:
    t-=1
    n = int(sys.stdin.readline().strip())
    turn = n//10+1
    lis=[]
    while turn:
        turn-=1
        lis = lis+list(map(int, sys.stdin.readline().strip().split()))
    pq = []
    # print("lis: ",lis)

    answer=[]
    mid=lis[0]
    answer.append(mid)

    left_q=[] # max_heap
    right_q=[] # min_heap: insert -1*value
    cnt=0

    for item in (lis[1:]):
        if item>mid:
            heapq.heappush(right_q, item)
        else:
            heapq.heappush(left_q, -1*item)

        if cnt%2==1: 
            if len(right_q)> len(left_q): # if right queue is bigger move middle to left queue
                heapq.heappush(left_q, -1*mid)
                mid = heapq.heappop(right_q)
            elif len(right_q)<len(left_q): # if left queue is bigger move middle to right queue
                heapq.heappush(right_q, mid)
                mid = -heapq.heappop(left_q)
            answer.append(mid) # if size is same print middle
        cnt+=1
    
    l = len(answer)
    sys.stdout.write(str(l)+'\n') # print answer length
    for idx,item in enumerate(answer):
        sys.stdout.write(str(item)+' ') # print item
        if (idx+1)%10==0: # if printed 10 items, go to next line
            sys.stdout.write('\n')
    sys.stdout.write('\n')