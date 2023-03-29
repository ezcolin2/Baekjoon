import sys
from collections import deque
import heapq
input=sys.stdin.readline
count = [0]*1000001
n=int(input())
res=[-1]*n
arr=list(map(int, input().split()))
for i in arr:
    count[i]+=1
stack=[0]
for i in range(1, n):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
            res[stack.pop()] = arr[i]
    stack.append(i)
for i in res:
    print(i, end=' ')