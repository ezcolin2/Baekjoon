import sys
sys.setrecursionlimit(int(1e9))
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    temp_max=0 # 최대값
    temp_sum=0 # 총 매수 주식 가격
    res=0 # 총 이득
    for i in range(n-1 ,-1 ,-1): # 거꾸로 조사
        if arr[i]>temp_max: # 크면 최대값 갱신 
            temp_max=arr[i]
        else: # 작다면 해당 주식을 사고 최대값에 팜
            res+=temp_max-arr[i]
    print(res)