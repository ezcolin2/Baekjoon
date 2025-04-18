# 좋은 수열, 나쁜 수열 판단
def is_good_sequence(sequence):
    sequence = str(sequence)
    # left(시작 지점)을 증가시키면서 two pointer 적용
    # 시간 복잡도 : O(N^2)
    for left in range(len(sequence)):
        for right in range(left+1, len(sequence)):
            # 다르다면 right 증가
            if sequence[left] != sequence[right]:
                right+=1
                continue
            
            # 같다면 나쁜 수열인지 확인한다.
            length = right-left
            is_break = False
            for i in range(length):
                if right+i >= len(sequence):
                    is_break = True
                    break
                if sequence[left+i] != sequence[right+i]:
                    is_break = True
                    break
            # 모두 같다면 나쁜 수열
            if is_break:
                continue
            return False
    return True

# 그리디 + DFS 적용
# 각 자릿수에서는 무조건 1, 2, 3 중 가장 작은 값을 선택한다.
# 바로 이전 값과 동일한 값이 나오지 않게 주의한다.
# 계속 작은 값만 선택했기 때문에 처음으로 길이가 n이 되는 순간 그 값이 가장 작은 값이 된다.
result = 0
n = int(input())
def choose(current_length):
    global result
    if not is_good_sequence(result):
        return
    if current_length == n:
        print(result)
        exit()
    for i in range(1, 4):
        result = result*10+i
        choose(current_length+1)
        result = result//10
choose(0)