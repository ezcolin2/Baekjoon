import sys
input = sys.stdin.readline
# 1. 이전과 높이가 같다. => 계속 탐색
# 2. 이전보다 높이가 1 높다. => 이전 L개만큼이 현재보다 1 작아야 함. (범위 체크) (경사로 놓기)
# 3. 이전보다 높이가 1 낮다. => 이후 L개만큼이 현재랑 같아야 함. (범위 체크) (경사로 놓기)
# 4. 1, 2, 3이 아니라면? => 지나갈 수 없는 길

# 2, 3번의 경우 경사로를 놓는데 이미 경사로가 있다면? -> 지나갈 수 없는 길

n, l = map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]

cnt=0 #갈 수 있는 길 수 
#가로 n줄 탐색
for i in range(n):
    ramp=[False]*n #경사로 여부
    cant_go = False #갈 수 없는지
    for j in range(1, n):
        if graph[i][j]==graph[i][j-1]:
            continue
        if graph[i][j]==graph[i][j-1]+1:
            for k in range(1, l+1): #이전 L개 탐색
                if j-k<0 or ramp[j-k] or graph[i][j]!=graph[i][j-k]+1: #범위를 벗어나거나 경사로가 이미 있거나 1차이가 아니라면
                    cant_go=True #이중 반복문 빠져나오기
                    break#이중 반복문 빠져나오기
                ramp[j-k]=True #경사로 놓기
        elif graph[i][j]==graph[i][j-1]-1:
            for k in range(l): #자신 포함 이후 L개 탐색
                if j+k>=n or ramp[j+k] or graph[i][j-1]!=graph[i][j+k]+1: #범위를 벗어나거나 경사로가 이미 있거나 1차이가 아니라면
                    cant_go=True #이중 반복문 빠져나오기
                    break#이중 반복문 빠져나오기
                ramp[j+k]=True #경사로 놓기
        else:
            cant_go=True
            break

    if cant_go:#이중 반복문 빠져나오기
        continue#이중 반복문 빠져나오기
    cnt+=1 #여기까지 왔다면 갈 수 있는 길 

#세로 n줄 탐색
for i in range(n):
    ramp=[False]*n #경사로 여부
    cant_go = False #갈 수 없는지
    for j in range(1, n):
        if graph[j][i]==graph[j-1][i]:
            continue
        if graph[j][i]==graph[j-1][i]+1:
            for k in range(1, l+1): #이전 L개 탐색
                if j-k<0 or ramp[j-k] or graph[j][i]!=graph[j-k][i]+1: #범위를 벗어나거나 경사로가 이미 있거나 1차이가 아니라면
                    cant_go=True #이중 반복문 빠져나오기
                    break#이중 반복문 빠져나오기
                ramp[j-k]=True #경사로 놓기
        elif graph[j][i]==graph[j-1][i]-1:
            for k in range(l): #자신 포함 이후 L개 탐색
                if j+k>=n or ramp[j+k] or graph[j-1][i]!=graph[j+k][i]+1: #범위를 벗어나거나 경사로가 이미 있거나 1차이가 아니라면
                    cant_go=True #이중 반복문 빠져나오기
                    break#이중 반복문 빠져나오기
                ramp[j+k]=True #경사로 놓기
        else:
            cant_go=True
            break

    if cant_go:#이중 반복문 빠져나오기
        continue#이중 반복문 빠져나오기
    cnt+=1 #여기까지 왔다면 갈 수 있는 길 
print(cnt)