import sys
input=sys.stdin.readline
n, m = map(int, input().split())
matrix_a = [list(input().rstrip()) for _ in range(n)]
matrix_b = [list(input().rstrip()) for _ in range(n)]

 #A의 각 요소들이 바뀌어야하는 횟수. 정확히는 짝수번이냐 홀수번이냐. 1번이면 홀수, 0번이면 짝수
matrix=[[0]*m for _ in range(n)] 
for i in range(n):
    for j in range(m):
        if matrix_a[i][j]!=matrix_b[i][j]:
            matrix[i][j]=1
cnt=0 # 변형 횟수 
for i in range(n-2):
    for j in range(m-2):
        if matrix[i][j]==1:
            cnt+=1
            for a in range(i,i+3):
                for b in range(j, j+3):
                    matrix[a][b] = 0 if matrix[a][b]==1 else 1
                    
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            print(-1)
            exit()
print(cnt)
