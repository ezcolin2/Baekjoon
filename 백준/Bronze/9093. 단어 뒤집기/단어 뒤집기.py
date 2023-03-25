import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    arr.append(input().split())
for i in arr:
    for j in i:
        temp=list(j)
        temp.reverse()
        print(''.join(temp), end=' ')
    print()