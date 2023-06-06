import sys
from collections import deque
input=sys.stdin.readline
s=int(input())
visited=[[False]*1001 for _ in range(1001)] 
arr=[[0]*1001 for _ in range(1001)] #최단 시간
#visited[n][m] : 화면 n개, 클립보드 m개
visited[1][0]=True #첫 노드 방문
arr[1][0]=0 #첫 노드 방문은 0초
queue=deque()
queue.append((1, 0))
while queue:
    screen, clip = queue.popleft() #꺼내기
    if screen==s: #s개의 이모티콘을 만듦
        print(arr[screen][clip]) 
        exit()
    if not visited[screen][screen]: #1번 
        visited[screen][screen]=True
        arr[screen][screen]=arr[screen][clip]+1
        queue.append((screen, screen))
    if clip+screen<=1000 and not visited[screen+clip][clip] and clip>0: #2번
        visited[screen+clip][clip]=True
        arr[screen+clip][clip]=arr[screen][clip]+1
        queue.append((screen+clip, clip))
    if screen-1>=0 and not visited[screen-1][clip]: #3번
        visited[screen-1][clip]=True
        arr[screen-1][clip]=arr[screen][clip]+1
        queue.append((screen-1, clip))

    
