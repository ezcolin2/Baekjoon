S = input()
if S == S[::-1]:
    print(len(S))
else:
    # 문자열의 길이만큼 반복
    for i in range(len(S)):
        # 문자열의 i번째부터 팰린드롬이라면
        if S[-1:i-1:-1] == S[i:]:
            # 문자열 i 이전 문자들을 문자열 뒤에
            # 독같이 추가하여 팰린드롬을 만든다.
            print(len(S)+i)
            break