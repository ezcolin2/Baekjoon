def is_possible(m): #길이가 m인 부분합 중 s 이상이면 true 반환
    for i in range(len(arr)-m):
        subtotal = arr[i+m]-arr[i] # 길이가 n인 부분합
        if subtotal >= s:
            return True
    return False
import sys
input=sys.stdin.readline
n, s = map(int, input().split())
arr=list(map(int, input().split()))
for i in range(1, n): #누적합 구함
    arr[i]+=arr[i-1]
arr.insert(0, 0)
if arr[-1]<s:#모두 다 더해도 s보다 작으면 0 출력
    print(0)
    exit()
left=1
right=len(arr)
res=1e5 #계속 갱신해야하는 최소 합
while left<=right:
    mid=(left+right)//2
    if is_possible(mid):
        res=min(res, mid)
        right=mid-1 #가장 짧은 길이를 출력해야해서
    else:
        left=mid+1
print(res)        
