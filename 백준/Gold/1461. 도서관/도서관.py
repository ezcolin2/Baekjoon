# 백준 1461
# 가장 먼 곳부터 책을 갖다놓으면 됨
import sys
input=sys.stdin.readline
n, m = map(int, input().split())
arr=list(map(int, input().split()))
# 양수, 음수를 나눔.
# 나누지 않으면 양수가 하나고 m이 2일 경우 문제가 생김
arr_positive=[]
arr_negative=[]
for i in arr:
    if i>0:
        arr_positive.append(i)
    else:
        arr_negative.append(-i)
arr_positive.sort()
arr_negative.sort()
res=0 # 걸음 수
    
#음수만 있거나 음수의 절대 값이 양수보다 클 때
if not arr_positive and arr_negative:
    res+=arr_negative[-1]
    temp=m
    while temp>0 and arr_negative:
        arr_negative.pop()
        temp-=1
elif not arr_negative and arr_positive:
    res+=arr_positive[-1]
    temp=m
    while temp>0 and arr_positive:
        arr_positive.pop()
        temp-=1
elif arr_negative[-1]>arr_positive[-1]:
    res+=arr_negative[-1]
    temp=m
    while temp>0 and arr_negative:
        arr_negative.pop()
        temp-=1
else:
    res+=arr_positive[-1]
    temp=m
    while temp>0 and arr_positive:
        arr_positive.pop()
        temp-=1

# 가장 멀리 있는 책은 정리 완료
# 이제부터 가장 멀리 있는 곳 부터 책을 놓으면 됨
# 지금부터는 왕복해야 됨

while arr_positive: # 빌 때까지
    temp=m-1
    res+=2*arr_positive.pop()
    while temp>0 and arr_positive:
        arr_positive.pop()
        temp-=1
while arr_negative: # 빌 때까지
    temp=m-1
    res+=2*arr_negative.pop()
    while temp>0 and arr_negative:
        arr_negative.pop()
        temp-=1
print(res)