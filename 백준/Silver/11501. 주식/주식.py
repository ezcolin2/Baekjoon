import sys
sys.setrecursionlimit(int(1e9))
input=sys.stdin.readline
arr=[]
dp=[] # dp[i]=m 의 뜻은 인덱스 i부터 끝까지 가장 큰 값이 m이라는 것을 의미
def get_max(left, right): # left부터 right까지 최대 가격 구함
    # temp_idx=left # 최대값의 인덱스
    if left==right:
        return 0
    # for i in range(left, right+1): # 우선 해당 범위의 최대값과 인덱스 구 함
    #     if arr[i]>arr[temp_idx]:
    #         temp_idx=i
    if dp[left]==left: # 첫 날이 가장 비싸면 그 다음날부터 이득 조사
        return get_max(left+1, right)
    elif dp[left]==right: # 마지막 날이 가장 비싸면 다 사고 마지막 날 팔면 됨
        temp_sum=0
        for i in range(left, right):
            temp_sum+=arr[i]
        return (arr[dp[left]])*(right-left)-temp_sum
    else: # 중간이 가장 비싸면 나눔
        return get_max(left, dp[left])+get_max(dp[left]+1, right)
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split())) # 날마다 주가
    dp=[0]*len(arr)
    dp[-1]=len(arr)-1
    temp_idx=dp[-1]
    temp_max=dp[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i]>arr[temp_idx]:
            temp_idx=i
        dp[i]=temp_idx
    print(get_max(0, n-1))