# 백준 2590
# 그리디
import sys
input=sys.stdin.readline
arr=[int(input()) for _ in range(6)]
cnt=0 # 판의 개수
cnt+=arr[5] # 6cm 색종이 하나는 무조건 판 하나 필요
cnt+=arr[4] # 5cm 색종이 하나는 무조건 판 하나 필요
cnt+=arr[3] # 4cm 색종이 하나는 무조건 판 하나 필요
cnt+=(arr[2]+3)//4 # 판 하나에 3cm 색종이 4개 들어갈 수 있음
three=36-9*(arr[2]%4) # 
two=5*arr[3] # 칸의 남은 자리 중 2cm가 들어갈 수 있는 자리
one=11*arr[4] # 칸의 남은 자리 중 1cm가 들어갈 수 있는 자리
if three==27:
    two+=5
    one+=7
elif three==18:
    two+=3
    one+=6
elif three==9:
    two+=1
    one+=5
if arr[1]<=two: # 만약 칸의 남은 자리에 2cm가 모두 들어갈 수 있다면
    one+=(two-arr[1])*4 # 2cm 모두 넣고 남은 자리는 1cm가 들어갈 수 있음 
    if arr[0]>one: # 만약 칸의 남은 자리에 1cm가 모두 들어갈 수 없다면 칸 추가
        arr[0]-=one
        while arr[0]>0: # 1cm가 모두 들어갈 수 있을 때까지 칸 추가
            cnt+=1
            arr[0]-=36
else: # 만약 칸의 남은 자리에 2cm가 모두 들어갈 수 없다면
    arr[1]-=two
    while arr[1]>0:
        cnt+=1
        arr[1]-=9
    one+=abs(arr[1])*4
    if arr[0]>one: # 만약 칸의 남은 자리에 1cm가 모두 들어갈 수 없다면 칸 추가
        arr[0]-=one
        while arr[0]>0: # 1cm가 모두 들어갈 수 있을 때까지 칸 추가
            cnt+=1
            arr[0]-=36
print(cnt)