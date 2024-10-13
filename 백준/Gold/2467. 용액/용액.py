def get_closest_zero_number(a, b):
    a = abs(a)
    b = abs(b)
    return min(a, b)
# 모두 양수인지
def is_all_plus(arr):
    return arr[0] >= 0

# 모두 음수인지
def is_all_minus(arr):
    return arr[-1] <= 0

# 처음으로 양수가 되는 인덱스 구하기 
def get_first_plus_index(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] >= 0:
            return i

def solution(arr):
    n = len(arr)
    if is_all_plus(arr):
        return 0, 1
    if is_all_minus(arr):
        return -2, -1
    
    # 처음으로 양수가 되는 인덱스를 구한다.
    first_plus_idx = get_first_plus_index(arr)
    left, right = first_plus_idx-1, first_plus_idx
    res = abs(arr[left]+arr[right])

    res_left, res_right = left, right
    # 범위에서 벗어나지 않을 때까지 반복한다.
    while left >= 0 and right < n:
        sum_value = arr[left]+arr[right]
        new_number = abs(sum_value)
        
        # 0에 더 가깝다면 갱신
        if new_number < res:
            res = new_number
            res_left, res_right = left, right
            
        # 만약 양수라면 더욱 작은 값을 넣어서 0에 가까운지 확인한다.
        if sum_value > 0:
            left -= 1
            continue
        # 만약 음수라면 더욱 큰 값을 넣어서 0에 가까운지 확인한다.
        if sum_value < 0:
            right += 1
            continue
        
        # 0이라면 종료
        return (res_left, res_right)
    if first_plus_idx < n-1:
        new_number = abs(arr[first_plus_idx]+arr[first_plus_idx+1])
        if new_number < res:
            res = new_number
            res_left, res_right = first_plus_idx, first_plus_idx+1
    elif first_plus_idx > 1:
        new_number = abs(arr[first_plus_idx-1]+arr[first_plus_idx-2])
        if new_number < res:
            res = new_number
            res_left, res_right = first_plus_idx-2, first_plus_idx-1
    return (res_left, res_right)

n = int(input())
arr = list(map(int, input().split())) 
left, right = solution(arr)
print(arr[left], arr[right])