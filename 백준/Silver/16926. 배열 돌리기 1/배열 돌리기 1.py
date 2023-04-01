import sys
import copy
def is_end(x, y): #방향 바꿀 조건
    return x in [sm, em] and y in [sn, en]
input=sys.stdin.readline
n, m, r = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
sn=0 #첫 행
en=n-1 #끝 행
sm=0 #첫 열
em=m-1 #끝 열
dx = [1, 0, -1, 0] #열 방향
dy = [0, 1, 0, -1] #행 방향
for _ in range(r): #r번 반복
    sn=0 #첫 행
    en=n-1 #끝 행
    sm=0 #첫 열
    em=m-1 #끝 열
    while sn<en and sm<em: #가장 안쪽까지
        x=sm
        y=sn
        #시작 점 임시 저장
        temp=arr[sn][sm]
        for i in range(4): # 4방향
            while True: #끝까지
                nx=x+dx[i]
                ny=y+dy[i]
                arr[y][x]=arr[ny][nx]
                if nx==sm and ny==sn:
                    arr[y][x]=temp
                x=nx
                y=ny
                if is_end(x, y): #끝이라면?
                    break
        sn+=1
        en-=1
        sm+=1
        em-=1
for i in arr:
    for j in i:
        print(j, end=' ')
    print()