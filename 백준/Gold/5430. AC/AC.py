import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    p=input().strip('\n')
    n=int(input())
    dq=deque(input().replace('[','').replace(']','').rstrip().split(','))
    left=True
    for i in p:
        con=False
        if i=='R':
            left= False if left else True
        elif n==0:
            print("error")
            con=True
            break
        elif left:
            dq.popleft()
            n-=1
        else:
            dq.pop()
            n-=1
    if con:
        continue
    if not left:
        dq.reverse()
    print("["+",".join(dq)+"]")