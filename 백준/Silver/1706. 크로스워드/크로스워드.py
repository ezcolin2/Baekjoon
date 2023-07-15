# 백준 1461
# 가장 먼 곳부터 책을 갖다놓으면 됨
import sys
input=sys.stdin.readline
r, c = map(int, input().split())
arr=[list(input().rstrip()) for _ in range(r)]
res='z'*20 # 사전 상 가장 뒤에 있는 단어. 이보다 앞서면 갱신.

# 가로부터 조사
for i in range(r):
    temp=''
    for j in range(c):
        if arr[i][j]!='#': # 확장 가능하다면
            temp+=arr[i][j]
        if j==c-1 or arr[i][j]=='#': # 확장 할 수 없다면
            if len(temp)>1: # 연속되었다면
                res=min(res, temp)
            temp=''

# 세로부터 조사
for i in range(c):
    temp=''
    for j in range(r):
        if arr[j][i]!='#': # 확장 가능하다면
            temp+=arr[j][i]
        if j==r-1 or arr[j][i]=='#': # 확장 할 수 없다면
            if len(temp)>1: # 연속되었다면
                res=min(res, temp)
            temp=''
print(res)