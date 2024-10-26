# 최소 점수를 score이상으로 받는 그룹으로 나누는 것이 가능한지
def is_possible_score(arr, k, min_score):
    group_cnt = 0 # 그룹 수
    score_sum = 0 # 점수 합
    for score in arr:
        score_sum += score
        # 접수 합이 최소 점수를 넘으면
        if score_sum >= min_score:
            # 그룹 수를 늘리고 점수 합을 0으로 초기화 한다.
            group_cnt += 1
            score_sum = 0
    return group_cnt >= k

def get_max_score(arr, k):
    left, right = 0, 2000000
    res = 0
    while left <= right:
        mid = (left+right)//2
        
        # 가능하다면 더욱 큰 값을 찾는다.
        if is_possible_score(arr, k, mid):
            left = mid+1
            res = max(res, mid)
            continue
        
        # 불가능하다면 더욱 작은 값을 찾는다.
        right = mid-1
    return res

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(get_max_score(arr, k))
