import sys
input=sys.stdin.readline
moeum=set(['a', 'e', 'i', 'o', 'u'])
while True:
    s=input().rstrip()
    if s=='end':
        break

    # 모음 포함 여부 확인
    is_moeum=False
    for i in moeum:
        if i in s: #모음이 있다면 
            is_moeum=True
    
    # 모음, 자음 3개 연속 여부
    not_continuity=True
    continuity=1    
    for i in range(1, len(s)):
        # 모음 연속
        if s[i] in moeum:
            if s[i-1] in moeum:
                continuity+=1
            else:
                continuity=1
        # 자음 연속 
        else:
            if s[i-1] not in moeum:
                continuity+=1
            else:
                continuity=1
        if continuity==3: # 3번 연속
            not_continuity=False
    
    # 같은 문자 여부 확인
    no_double_char=True
    for i in range(1, len(s)):
        if s[i]==s[i-1]: #같음 
            if s[i]!='e' and s[i]!='o':
                no_double_char=False

    if is_moeum and not_continuity and no_double_char:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")