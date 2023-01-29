import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dq=deque(list(map(int, input().split())))
    res=0
    while len(dq)!=1:
        b=False
        for i in range(1, len(dq)):
            if dq[i]>dq[0]:
                dq.append(dq.popleft())
                m-=1
                if m<0:
                    m=len(dq)-1
                b=True
                break
        if b:
            continue
        if m==0:
            break

        dq.popleft()
        res+=1
        m-=1
    print(res+1)