# m명의 조카들에게 snack_length만큼 나눠주는 것이 가능한가
def is_possible(arr, m, snack_length):
    if snack_length == 0:
        return False
    cnt = 0 # snack_length만큼의 과자 개수
    for snack in arr:
        cnt += snack//snack_length
    return cnt >= m
m, n = map(int, input().split())
arr = list(map(int, input().split()))

# 이진 탐색 시작
res = 0
left, right = 1, 1000000000
while left <= right:
    mid = (left + right)//2
    if is_possible(arr, m, mid):
        res = max(res, mid)
        left = mid + 1
        continue
    right = mid - 1
print(res)