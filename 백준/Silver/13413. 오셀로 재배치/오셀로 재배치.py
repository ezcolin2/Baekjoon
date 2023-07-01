import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    w=0 # w로 바꿔야 하는 말의 개수 
    b=0 # b로 바꿔야 하는 말의 개수 
    n=int(input())
    s_from=input().rstrip() # 처음 상태
    s_to=input().rstrip() # 바꿔야 하는 상태
    for i in range(len(s_from)):
        if s_from[i]=='W' and s_to[i]=='B':
            b+=1
        elif s_from[i]=='B' and s_to[i]=='W':
            w+=1
    cnt=0 # 작업 횟수
    while w>0 and b>0: # 1번 연산 시작
        cnt+=1
        b-=1
        w-=1
    cnt+=b+w
    print(cnt)
    
