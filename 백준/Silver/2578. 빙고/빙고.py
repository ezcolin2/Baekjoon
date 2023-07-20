# 백준 2578
import sys
from collections import deque
input=sys.stdin.readline

height = [5]*5 # height[0]=2의 의미는 0번 열이 빙고가 되기까지 남은 수의 개수
width = [5]*5 # width[0]=2의 의미는 0번 행이 빙고가 되기까지 남은 수의 개수
right_diagonal = 5 # 오른쪽 아래 방향 대각선
left_diagonal = 5 # 왼쪽 아래 방향 대각선

position={} # key = 수, value는 위치

# 딕셔너리에 모든 수의 위치를 저장
for row in range(5):
    temp=list(map(int, input().split()))
    for col, val in enumerate(temp):
        position[val] = (row, col)

arr=[list(map(int, input().split())) for _ in range(5)]

cnt=0 # 빙고 수
for i in range(5):
    for j in range(5):
        num = arr[i][j] # 사회자가 부른 수
        row, col = position[num] # 그 수의 빙고판 위치
        width[row]-=1
        height[col]-=1
        if row==col:
            right_diagonal-=1
        if row+col==4:
            left_diagonal-=1

        if width[row]==0:
            cnt+=1
        if height[col]==0:
            cnt+=1
        if right_diagonal==0:
            cnt+=1
            right_diagonal-=1 # 중복 방지
        if left_diagonal==0:
            cnt+=1
            left_diagonal-=1 # 중복 방지 
        if cnt>=3:
            print(i*5+j+1)
            exit()
