import sys
from collections import deque
input=sys.stdin.readline
string=list(input().rstrip())
arr=deque()
for i in string:
    arr.append(i)
n=int(input())
idx=len(arr) #커서의 현재 위치
for _ in range(n):
    command =input().split()
    if len(command)==2: #커서 왼쪽에 추가
        arr.append(command[1])
        idx+=1
    else:
        if command[0]=='L':
            if idx>0:
                arr.appendleft(arr.pop())
                idx-=1
        elif command[0]=='D':
            if idx<len(arr):
                arr.append(arr.popleft())
                idx+=1
        elif command[0]=='B':
            if idx>0:
                arr.pop()
                idx-=1
while idx<len(arr):
    arr.append(arr.popleft())
    idx+=1
for i in arr:
    print(i, end='')