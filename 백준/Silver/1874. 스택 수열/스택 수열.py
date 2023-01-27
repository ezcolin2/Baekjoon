import sys
# 입력으로 들어온 값이 last_input보다 작으면?
#     =>stack[-1]값과 입력값 비교 입력값이 더 크거나 스택이 비어있으면?
#         =>불가능
#     =>아니면?
#         =>나올때까지 pop하기
#          =>계속 stack[-1]과 비교
# 크면?
#     =>last_input 증가시키면서 스택에 넣기
# 교교
n=int(sys.stdin.readline())
last_input=1
stack=[]
res=''
for _ in range(n):
    temp=int(sys.stdin.readline())
    if temp>=last_input:
        while last_input<=temp:
            stack.append(last_input)
            last_input+=1
            res+='+'
        stack.pop()
        res+='-'
    else:
        if len(stack)==0:
            print("NO")
            exit()
        else:
            while stack.pop()!=temp:
                res+='-'
                if len(stack)==0:#다 꺼냈는데 안 나옴
                    print("NO")
                    exit()
            #통과했다는건 나왔다는 뜻
            res+='-'
for i in res:
    print(i)