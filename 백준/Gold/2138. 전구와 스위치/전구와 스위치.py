import sys
input=sys.stdin.readline
n=int(input())
bulb=list(input().rstrip())
switch=list(input().rstrip())
#전구의 상태를 홀수번 바꿔야하면 1 짝수번 바꿔야하면 0
arr=[
    1 if bulb[i]!=switch[i] else 0 
    for i in range(n)
]

#n-1, n, n+1 문제를 n, n+1, n+2로 변형한다.
#그래서 맨 앞에 0을 넣은 것 한 번, 1을 넣은 것 한 번 총 두 번을 실시한다.

arr_temp=[0]+arr
cnt_1=0 #변형 횟수 
possible_1=True # 가능 여부
for i in range(n-1):
    if arr_temp[i]==1:
        cnt_1+=1
        for j in range(i, i+3):
            arr_temp[j]=0 if arr_temp[j]==1 else 1
if arr_temp[n-1]!=arr_temp[n]: #불가능한 상황
    possible_1=False
elif arr_temp[n-1]==1 and arr_temp[n]==1: #둘 다 1이면 한 번 더 바꿔야하곡 둘 다 0이면 끝 
    cnt_1+=1

arr_temp=[1]+arr
cnt_2=0 #변형 횟수 
possible_2=True # 가능 여부
for i in range(n-1):
    if arr_temp[i]==1:
        cnt_2+=1
        for j in range(i, i+3):
            arr_temp[j]=0 if arr_temp[j]==1 else 1
if arr_temp[n-1]!=arr_temp[n]: #불가능한 상황
    possible_2=False
elif arr_temp[n-1]==1 and arr_temp[n]==1: #둘 다 1이면 한 번 더 바꿔야하곡 둘 다 0이면 끝 
    cnt_2+=1

if possible_1 and possible_2: #둘 다 가능하다면 작은 값
    print(min(cnt_1, cnt_2))
elif possible_1: #1번만 가능하다면 
    print(cnt_1)
elif possible_2: #2번만 가능하다면 
    print(cnt_2)
else: #둘 다 안된다면 
    print(-1)