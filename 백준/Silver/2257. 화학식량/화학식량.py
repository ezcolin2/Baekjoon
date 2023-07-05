import sys
from collections import deque
input=sys.stdin.readline
s=input().rstrip()
value={'H':1, 'C':12, 'O':16}
stack=deque()
res=0
for i in s:
    if i=='(':
        stack.append(i)
    elif i==')': # '('가 나올 때까지 다 더함
        temp=0
        while True:
            pop_value=stack.pop()
            if pop_value=='(':
                break
            temp+=pop_value
        stack.append(temp) # 합을 다시 스택에 넣음
    elif i.isdigit(): # 숫자라면 스택에서 빼서 숫자만큼 다시 넣기
        pop_value=stack.pop()
        stack.append(pop_value*int(i))
    else:
        stack.append(value[i])
print(sum(stack))