def is_possible(arr, n, l, min_len):
    last_num = 0
    slice_cnt = 0
    temp_arr = arr[:]+[l]
    for num in temp_arr:
        # 잘라도 괜찮다면
        if num-last_num >= min_len:
            slice_cnt += 1
            last_num = num
            
    return slice_cnt > n


def get_max_len(arr, slice_cnt, l):
    res = 0
    left, right = 0, l
    while left<=right:
        mid = (left+right)//2
        if is_possible(arr, slice_cnt, l, mid):
            left=mid+1
            res = max(res, mid)
        else:
            right=mid-1
    return res

n, m, l = map(int, input().split())
arr = [int(input()) for _ in range(m)]
slice_arr = [int(input()) for _ in range(n)]
for slice_cnt in slice_arr:
    print(get_max_len(arr, slice_cnt, l))