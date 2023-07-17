# 백준 1715
# 그리디
import sys
import heapq
input=sys.stdin.readline
n=int(input())
queue=[]
for _ in range(n):
    heapq.heappush(queue, int(input()))
cnt=0 # 비교 횟수
while len(queue)>1: # 큐가 빌 때까지
    a=heapq.heappop(queue)
    b=heapq.heappop(queue)
    cnt+=a+b
    heapq.heappush(queue, a+b)
print(cnt)