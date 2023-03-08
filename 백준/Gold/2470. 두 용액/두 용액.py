import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int ,input().split()))
arr.sort()
left=0
right=len(arr)-1
like_zero=arr[left]+arr[right] #0에 가장 가까운 수
res=[arr[left], arr[right]] #결과값
while left<right:
    add=arr[left]+arr[right]
    if abs(add)<abs(like_zero): #0에 더 가까운 수가 나오면 갱신
        like_zero=add
        res[0]=arr[left]
        res[1]=arr[right]
    if add==0:
        break
    elif add>0:
        right-=1
    else:
        left+=1
print(res[0], res[1])