import sys
from collections import deque
import heapq
input=sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))
heap=[(arr[0], 0)] #첫 번째는 값 두 번째는 인덱스
res=[-1]*n #각각의 인덱스에 대한 오큰수 값
for i in range(1, n):
    while True:
        temp=heapq.heappop(heap) #가장 작은 값 꺼냄
        if temp[0]<arr[i]: #꺼낸 값이 현재 위치보다 작으면
            res[temp[1]]=arr[i] #오큰수 저장
        else:
            heapq.heappush(heap, temp) #꺼낸 값이 크면 다시 최소 힙에 넣음
            break
        if len(heap)==0:
            break
    
    heapq.heappush(heap, (arr[i], i)) #최소 힙에 넣기
for i in res:
    print(i, end=' ')